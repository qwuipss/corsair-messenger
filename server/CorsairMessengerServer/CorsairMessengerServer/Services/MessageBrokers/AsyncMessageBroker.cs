using CorsairMessengerServer.Data.Entities;
using CorsairMessengerServer.Data.Entities.Request.Message;
using CorsairMessengerServer.Data.Entities.Response.Message;
using CorsairMessengerServer.Data.Repositories;
using System.Net.WebSockets;
using System.Text;
using System.Text.Json;

namespace CorsairMessengerServer.Services.MessageBrokers
{
    public class AsyncMessageBroker : IMessageBroker
    {
        private readonly WebSocketsRepository _webSocketsRepository;

        private readonly MessagesRepository _messagesRepository;

        public AsyncMessageBroker(WebSocketsRepository webSocketsRepository, MessagesRepository messagesRepository)
        {
            _webSocketsRepository = webSocketsRepository;
            _messagesRepository = messagesRepository;
        }

        public async Task SendMessageAsync(MessageEntity message)
        {
            if (message.SenderId != message.ReceiverId)
            {
                await AddMessageToRepositoryAsync(message);
                await SendMessageIfPossibleAsync(message);
                await SendMessageDeliveryCallbackIfPossibleAsync(message);
            }
        }

        private static byte[] GetMessageDeliveryResponse(MessageEntity message)
        {
            var serializedMessage = JsonSerializer.Serialize(new MessageDeliveryResponseEntity
            {
                Type = (int)MessageDeliveryBaseEntity.MessageResponseEntityType.New,
                Id = message.Id,
                Text = message.Text,
                SenderId = message.SenderId,
                SendTime = message.SendTime,
            });

            return GetBytes(serializedMessage);
        }

        private static byte[] GetSerializedMessageDeliveryCallback(MessageEntity message)
        {
            var serializedMessage = JsonSerializer.Serialize(new MessageDeliveryCallbackEntity
            {
                Type = (int)MessageDeliveryBaseEntity.MessageResponseEntityType.Callback,
                Id = message.Id,
                UserId = message.ReceiverId,
                Text = message.Text,
                SendTime = message.SendTime,
            });

            return GetBytes(serializedMessage);
        }

        private static async Task SendMessageIfPossibleAsync(byte[] buffer, WebSocket receiverSocket)
        {
            if (receiverSocket.State is WebSocketState.Open)
            {
                await receiverSocket.SendAsync(
                    new ArraySegment<byte>(buffer), WebSocketMessageType.Text, true, CancellationToken.None);
            }
        }

        private async Task SendMessageIfPossibleAsync(MessageEntity message)
        {
            if (_webSocketsRepository.TryGetWebSocket(message.ReceiverId, out var receiverSocket))
            {
                var buffer = GetMessageDeliveryResponse(message);

                await SendMessageIfPossibleAsync(buffer, receiverSocket);
            }
        }

        private async Task SendMessageDeliveryCallbackIfPossibleAsync(MessageEntity message)
        {
            if (_webSocketsRepository.TryGetWebSocket(message.SenderId, out var receiverSocket))
            {
                var buffer = GetSerializedMessageDeliveryCallback(message);

                await SendMessageIfPossibleAsync(buffer, receiverSocket);
            }
        }

        private async Task AddMessageToRepositoryAsync(MessageEntity message)
        {
            await _messagesRepository.AddMessageAsync(message);
        }

        private static byte[] GetBytes(string serializedMessage)
        {
            return Encoding.UTF8.GetBytes(serializedMessage);
        }
    }
}
