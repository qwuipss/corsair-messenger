using CorsairMessengerServer.Models.Message;

namespace CorsairMessengerServer.Services.MessageBrokers
{
    public interface IMessageBroker
    {
        public Task DeliverMessage(MessageSendingRequest request);
    }
}
