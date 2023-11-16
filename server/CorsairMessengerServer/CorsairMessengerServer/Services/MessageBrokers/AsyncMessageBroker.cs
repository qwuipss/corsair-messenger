using CorsairMessengerServer.Data.Entities;
using CorsairMessengerServer.Data.Repositories;
using Microsoft.EntityFrameworkCore.Metadata.Internal;
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
            await AddMessageToRepositoryAsync(message);

            await SendMessageIfPossibleAsync(message);

            await SendMessageDeliveredToServerSignal(message);
        }

        private static byte[] GetSerializedMessage(MessageEntity message)
        {
            var serializedMessage = JsonSerializer.Serialize(new 
            { 
                id = message.Id, 
                sender_id = message.SenderId, 
                text = message.Text, 
                send_time = message.SendTime,
            });

            var buffer = Encoding.UTF8.GetBytes(serializedMessage);

            return buffer;
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
                var buffer = GetSerializedMessage(message);

                await SendMessageIfPossibleAsync(buffer, receiverSocket);
            }
        }

        private async Task SendMessageDeliveredToServerSignal(MessageEntity message)
        {
            var callbackMessage = new { message_id = message.Id };

            if (_webSocketsRepository.TryGetWebSocket(message.SenderId, out var receiverSocket))
            {
                var buffer = GetSerializedMessage(message);

                await SendMessageIfPossibleAsync(buffer, receiverSocket);
            }
        }

        private async Task AddMessageToRepositoryAsync(MessageEntity message)
        {
            await _messagesRepository.AddMessageAsync(message);
        }
    }
}
