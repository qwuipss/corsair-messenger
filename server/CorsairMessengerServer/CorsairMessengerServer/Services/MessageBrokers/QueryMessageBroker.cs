using CorsairMessengerServer.Data.Repositories.WebSockets;
using CorsairMessengerServer.Models.Message;

namespace CorsairMessengerServer.Services.MessageBrokers
{
    public class QueryMessageBroker : IMessageBroker
    {
        private readonly IWebSocketsRepository _webSocketsRepository;

        public QueryMessageBroker(IWebSocketsRepository webSocketsRepository) 
        { 
            _webSocketsRepository = webSocketsRepository;
        }

        public async Task DeliverMessage(MessageSendingRequest request)
        {
            if (_webSocketsRepository.TryGetWebSocket(request.RecieverId, out var receiverSocket))
            {
                //receiverSocket.SendAsync();
            }
        }
    }
}
