using CorsairMessengerServer.Data.Entities.Message;
using CorsairMessengerServer.Data.Repositories;
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

        private readonly WebSocketsRepository _webSocketsRepository;

        private readonly IMessageBroker _messageBroker;

        public WebSocketsManager(WebSocketsRepository webSocketsRepository, IMessageBroker messageBroker)
        {
            _webSocketsRepository = webSocketsRepository;
            _messageBroker = messageBroker;
        }

        public WebSocketConnection OnConnected(int socketId, WebSocket webSocket)
        {
            var webSocketConnection = new WebSocketConnection(socketId, webSocket);

            _webSocketsRepository.AddWebSocket(socketId, webSocket);

            return webSocketConnection;
        }

        public async Task OnDisconnectedAsync(WebSocketConnection webSocketConnection)
        {
            await _webSocketsRepository.RemoveWebSocketAsync(webSocketConnection.SocketId);
        }

        public async Task StartReceivingAsync(WebSocketConnection webSocketConnection)
        {
            var socketId = webSocketConnection.SocketId;
            var webSocket = webSocketConnection.WebSocket;

            var buffer = new byte[MESSAGE_RECEIVE_BUFFER_SIZE];
            var contentBuilder = new List<byte>();

            while (webSocket.State is WebSocketState.Open)
            {
                WebSocketReceiveResult receiveResult;

                try
                {
                    receiveResult = await webSocket.ReceiveAsync(new ArraySegment<byte>(buffer), CancellationToken.None);
                }
                catch (WebSocketException)
                {
                    break;
                }

                if (receiveResult.MessageType is WebSocketMessageType.Text)
                {
                    if (ReceiveMessage(buffer, receiveResult, contentBuilder))
                    {
                        var message = await TryParseMessageAsync(contentBuilder.ToArray(), socketId);

                        if (message is not null)
                        {
                            await SendMessageAsync(message);

                            contentBuilder = new List<byte>();
                        }
                    }

                    await PauseReceivingAsync();
                }
                else if (receiveResult.MessageType is WebSocketMessageType.Close)
                {
                    break;
                }
            }

            await OnDisconnectedAsync(webSocketConnection);
        }

        private static bool ReceiveMessage(byte[] buffer, WebSocketReceiveResult receiveResult, List<byte> contentBuilder)
        {
            contentBuilder.ReceiveBytes(buffer, receiveResult);

            return receiveResult.EndOfMessage;
        }

        private static async Task<Message?> TryParseMessageAsync(byte[] buffer, int socketId)
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
        private static async Task PauseReceivingAsync()
        {
            await Task.Delay(RECEIVING_PAUSE_DELAY_MS);
        }

        private async Task SendMessageAsync(Message message)
        {
            await _messageBroker.SendMessageAsync(message);
        }
    }
}
