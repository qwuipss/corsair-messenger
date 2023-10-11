using CorsairMessengerServer.Data.Entities.Message;

namespace CorsairMessengerServer.Services.MessageBrokers
{
    public interface IMessageBroker
    {
        public void SendMessage(Message message);

        public void StartSendingMessages();
    }
}
