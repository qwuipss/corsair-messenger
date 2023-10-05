using CorsairMessengerServer.Models.Message;

namespace CorsairMessengerServer.Services.MessageBrokers
{
    public interface IMessageBroker
    {
        public void Send(MessageSendingRequest request);
    }
}
