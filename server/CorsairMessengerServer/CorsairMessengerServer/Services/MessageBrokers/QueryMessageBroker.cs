using CorsairMessengerServer.Data.Entities.Message;
using CorsairMessengerServer.Data.Repositories.WebSockets;

namespace CorsairMessengerServer.Services.MessageBrokers
{
    public class QueryMessageBroker : IMessageBroker
    {
        private readonly IWebSocketsRepository _webSocketsRepository;

        public QueryMessageBroker(IWebSocketsRepository webSocketsRepository) 
        { 
            _webSocketsRepository = webSocketsRepository;
        }

        public async Task DeliverMessage(Message request)
        {
            var receiverId = request.RecieverId;
            var buffer = request.Content;

            if (_webSocketsRepository.TryGetWebSocket(receiverId, out var receiverSocket))
            {
                //receiverSocket.SendAsync();
            }
        }
    }
}
