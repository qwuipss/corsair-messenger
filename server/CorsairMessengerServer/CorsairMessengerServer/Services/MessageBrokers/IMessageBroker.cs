using CorsairMessengerServer.Data.Entities.Message;

namespace CorsairMessengerServer.Services.MessageBrokers
{
    public interface IMessageBroker
    {
        public void DeliverMessage(Message message);

        public void StartSendingMessages();
    }
}
