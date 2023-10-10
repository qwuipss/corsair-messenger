using CorsairMessengerServer.Data.Entities.Message;
using CorsairMessengerServer.Data.Repositories.WebSockets;
using System.Collections.Concurrent;
using System.Net.WebSockets;
using System.Text;
using System.Text.Json;

namespace CorsairMessengerServer.Services.MessageBrokers
{
    public class QueryMessageBroker : IMessageBroker
    {
        private static readonly ConcurrentQueue<Message> _messagesQueue;

        private readonly IWebSocketsRepository _webSocketsRepository;

        private Thread? _newsletterThread;

        static QueryMessageBroker()
        {
            _messagesQueue = new ConcurrentQueue<Message>();
        }

        public QueryMessageBroker(IWebSocketsRepository webSocketsRepository)
        {
            _webSocketsRepository = webSocketsRepository;
        }

        public void StartSendingMessages()
        {
            if (_newsletterThread is not null)
            {
                throw new InvalidOperationException("messages sending already started");
            }

            _newsletterThread = new Thread(async () =>
            {
                while (true)
                {
                    if (_messagesQueue.TryDequeue(out var message))
                    {
                        await SendMessage(message);
                    }
                }
            });

            _newsletterThread.Start();
        }

        public void DeliverMessage(Message message)
        {
            _messagesQueue.Enqueue(message);
        }

        private async Task SendMessage(Message message)
        {
            var serializedMessage = JsonSerializer.Serialize(new { message.SenderId, message.Text });
            var buffer = Encoding.UTF8.GetBytes(serializedMessage);

            var receiverId = message.RecieverId;

            if (_webSocketsRepository.TryGetWebSocket(receiverId, out var receiverSocket))
            {
                await receiverSocket.SendAsync(
                    new ArraySegment<byte>(buffer), WebSocketMessageType.Text, true, CancellationToken.None);
            }
        }
    }
}
