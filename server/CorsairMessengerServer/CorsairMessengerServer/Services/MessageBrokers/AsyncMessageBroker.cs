using CorsairMessengerServer.Data.Entities;
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

        public async Task SendMessageAsync(Message message)
        {
            await AddMessageToRepositoryAsync(message);
            await SendMessageIfPossibleAsync(message);
        }

        private static byte[] GetSerializedMessage(Message message)
        {
            var serializedMessage = JsonSerializer.Serialize(new { message.SenderId, message.Text });

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

        private async Task SendMessageIfPossibleAsync(Message message)
        {
            if (_webSocketsRepository.TryGetWebSocket(message.RecieverId, out var receiverSocket))
            {
                var buffer = GetSerializedMessage(message);
                await SendMessageIfPossibleAsync(buffer, receiverSocket);
            }
        }

        private async Task AddMessageToRepositoryAsync(Message message)
        {
            await _messagesRepository.AddMessageAsync(message);
        }
    }
}
