using CorsairMessengerServer.Data.Entities.Message;
using CorsairMessengerServer.Data.Repositories;
using System.Collections.Concurrent;
using System.Net.WebSockets;
using System.Text;
using System.Text.Json;

namespace CorsairMessengerServer.Services.MessageBrokers
{
    public class QueryMessageBroker : IMessageBroker
    {
        private static readonly ConcurrentQueue<Message> _messagesQueue;

        private readonly WebSocketsRepository _webSocketsRepository;

        private readonly MessagesRepository _messagesRepository;

        private Thread? _messagesSendingThread;

        static QueryMessageBroker()
        {
            _messagesQueue = new ConcurrentQueue<Message>();
        }

        public QueryMessageBroker(WebSocketsRepository webSocketsRepository, MessagesRepository messagesRepository)
        {
            _webSocketsRepository = webSocketsRepository;
            _messagesRepository = messagesRepository;
        }

        public void StartSendingMessages()
        {
            if (_messagesSendingThread is not null)
            {
                throw new InvalidOperationException("messages sending already started");
            }

            _messagesSendingThread = new Thread(async () =>
            {
                while (true)
                {
                    if (_messagesQueue.TryDequeue(out var message))
                    {
                        var buffer = GetSerializedMessage(message);

                        await AddMessageToRepository(message);
                        await SendMessage(buffer, message);
                    }
                }
            })
            {
                Priority = ThreadPriority.AboveNormal
            };

            _messagesSendingThread.Start();
        }

        public void SendMessage(Message message)
        {
            _messagesQueue.Enqueue(message);
        }

        private static byte[] GetSerializedMessage(Message message)
        {
            var serializedMessage = JsonSerializer.Serialize(new { message.SenderId, message.Text });

            var buffer = Encoding.UTF8.GetBytes(serializedMessage);

            return buffer;
        }

        private async Task SendMessage(byte[] buffer, Message message)
        {
            if (_webSocketsRepository.TryGetWebSocket(message.RecieverId, out var receiverSocket))
            {
                await receiverSocket.SendAsync(
                    new ArraySegment<byte>(buffer), WebSocketMessageType.Text, true, CancellationToken.None);
            }
        }

        private async Task AddMessageToRepository(Message message)
        {
            await _messagesRepository.AddMessageAsync(message);
        }
    }
}
