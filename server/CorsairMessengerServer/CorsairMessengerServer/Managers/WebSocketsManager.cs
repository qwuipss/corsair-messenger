using CorsairMessengerServer.Data.Entities.Message;
using CorsairMessengerServer.Data.Repositories.WebSockets;
using CorsairMessengerServer.Extensions;
using CorsairMessengerServer.Services.MessageBrokers;
using System.Net.WebSockets;
using System.Text.Json;

namespace CorsairMessengerServer.Managers
{
    public class WebSocketsManager
    {
        public record WebSocketConnection(int SocketId, WebSocket WebSocket);

        private const int RECEIVING_PAUSE_DELAY_MS = 300;

        private const int MESSAGE_RECEIVE_BUFFER_SIZE = 1024;

        private readonly IWebSocketsRepository _webSocketsRepository;

        private readonly IMessageBroker _messageBroker;

        public WebSocketsManager(IWebSocketsRepository webSocketsRepository, IMessageBroker messageBroker)
        {
            _webSocketsRepository = webSocketsRepository;
            _messageBroker = messageBroker;

            _messageBroker.StartSendingMessages();
        }

        public WebSocketConnection OnConnected(int socketId, WebSocket webSocket)
        {
            var webSocketConnection = new WebSocketConnection(socketId, webSocket);

            _webSocketsRepository.AddWebSocket(socketId, webSocket);

            return webSocketConnection;
        }

        public void OnDisconnected(WebSocketConnection webSocketConnection)
        {
            _webSocketsRepository.RemoveWebSocket(webSocketConnection.SocketId);
        }

        public async Task StartReceiving(WebSocketConnection webSocketConnection)
        {
            var socketId = webSocketConnection.SocketId;
            var webSocket = webSocketConnection.WebSocket;

            var buffer = new byte[MESSAGE_RECEIVE_BUFFER_SIZE];
            var contentBuilder = new List<byte>();

            while (webSocket.State is WebSocketState.Open)
            {
                var receiveResult = await webSocket.ReceiveAsync(new ArraySegment<byte>(buffer), CancellationToken.None);

                if (receiveResult.MessageType is WebSocketMessageType.Text)
                {
                    if (ReceiveMessage(buffer, receiveResult, contentBuilder))
                    {
                        var message = await TryParseMessage(contentBuilder.ToArray(), socketId);

                        if (message is not null)
                        {
                            SendMessage(message);

                            contentBuilder.Clear();
                        }
                    }

                    await PauseReceiving();
                }
                else if (receiveResult.MessageType is WebSocketMessageType.Close)
                {
                    OnDisconnected(webSocketConnection);
                }
            }
        }

        private static bool ReceiveMessage(byte[] buffer, WebSocketReceiveResult receiveResult, List<byte> contentBuilder)
        {
            contentBuilder.ReceiveBytes(buffer, receiveResult);

            return receiveResult.EndOfMessage;
        }

        private static async Task<Message?> TryParseMessage(byte[] buffer, int socketId)
        {
            Message? message = null;

            try
            {
                var options = new JsonSerializerOptions
                {
                    PropertyNameCaseInsensitive = true,
                };

                var memoryStream = new MemoryStream(buffer);

                message = (await JsonSerializer.DeserializeAsync<Message>(memoryStream, options))!;
            }
            catch
            {
                return message;
            }

            message.SenderId = socketId;
            message.SendTime = DateTime.UtcNow;

            return message;
        }

        /// <summary>
        /// Needed for preventing memory leak due infinite loop message spam
        /// </summary>
        private static Task PauseReceiving()
        {
            return Task.Delay(RECEIVING_PAUSE_DELAY_MS);
        }

        private void SendMessage(Message message)
        {
            _messageBroker.DeliverMessage(message);
        }
    }
}
