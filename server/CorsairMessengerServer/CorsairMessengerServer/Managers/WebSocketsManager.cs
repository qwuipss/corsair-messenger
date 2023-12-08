using CorsairMessengerServer.Data.Entities;
using CorsairMessengerServer.Data.Entities.Request;
using CorsairMessengerServer.Data.Repositories;
using CorsairMessengerServer.Extensions;
using CorsairMessengerServer.Services.MessageBrokers;
using System.Net.Sockets;
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

        private readonly UsersRepository _usersRepository;

        private readonly IMessageBroker _messageBroker;

        public WebSocketsManager(WebSocketsRepository webSocketsRepository, UsersRepository usersRepository, IMessageBroker messageBroker)
        {
            _webSocketsRepository = webSocketsRepository;
            _usersRepository = usersRepository;
            _messageBroker = messageBroker;
        }

        public WebSocketConnection OnConnected(int socketId, WebSocket webSocket)
        {
            var webSocketConnection = new WebSocketConnection(socketId, webSocket);

            _webSocketsRepository.AddWebSocket(socketId, webSocket);

            return webSocketConnection;
        }

        public async Task ClosePreviousConnectionIfExist(int socketId)
        {
            if (_webSocketsRepository.TryGetWebSocket(socketId, out var previousWebSocket))
            {
                await previousWebSocket.CloseAsync(
                    WebSocketCloseStatus.PolicyViolation, "new connection detected", CancellationToken.None);
            }
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
                        var (IsParsed, Message, DeliveryRequest) = await TryParseMessageAsync(contentBuilder.ToArray(), socketId);

                        if (IsParsed)
                        {
                            if (await IsReceiverExist(Message!))
                            {
                                await SendMessageAsync(Message!, DeliveryRequest!);
                            }

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

        private async Task<bool> IsReceiverExist(MessageEntity message)
        {
            return await _usersRepository.IsUserExist(message.ReceiverId);
        }

        private static bool ReceiveMessage(byte[] buffer, WebSocketReceiveResult receiveResult, List<byte> contentBuilder)
        {
            contentBuilder.ReceiveBytes(buffer, receiveResult);

            return receiveResult.EndOfMessage;
        }

        private static async Task<(bool IsParsed, MessageEntity? Message, MessageDeliveryRequestEntity? DeliveryRequest)> TryParseMessageAsync(byte[] buffer, int socketId)
        {
            MessageDeliveryRequestEntity? messageRequest;

            try
            {
                var options = new JsonSerializerOptions
                {
                    PropertyNameCaseInsensitive = true,
                };

                var memoryStream = new MemoryStream(buffer);

                messageRequest = (await JsonSerializer.DeserializeAsync<MessageDeliveryRequestEntity>(memoryStream, options))!;
            }
            catch
            {
                return (false, null, null);
            }

            var message = BuildMessageEntity(socketId, messageRequest);

            return (true, message, messageRequest);
        }

        /// <summary>
        /// Needed for preventing memory leak due infinite loop message spam
        /// </summary>
        private static async Task PauseReceivingAsync()
        {
            await Task.Delay(RECEIVING_PAUSE_DELAY_MS);
        }

        private async Task SendMessageAsync(MessageEntity message, MessageDeliveryRequestEntity deliveryRequestMessage)
        {
            await _messageBroker.SendMessageDeliveryCallbackIfPossibleAsync(message, deliveryRequestMessage);
            await _messageBroker.SendMessageAsync(message);
        }

        private static MessageEntity BuildMessageEntity(int socketId, MessageDeliveryRequestEntity messageRequest)
        {
            return new MessageEntity
            {
                SenderId = socketId,
                ReceiverId = messageRequest.ReceiverId,
                Text = messageRequest.Text,
                SendTime = DateTime.UtcNow,
            };
        }

    }
}
