using CorsairMessengerServer.Data.Entities.Message;

namespace CorsairMessengerServer.Services.MessageBrokers
{
    public interface IMessageBroker
    {
        public Task SendMessageAsync(Message message);
    }
}
