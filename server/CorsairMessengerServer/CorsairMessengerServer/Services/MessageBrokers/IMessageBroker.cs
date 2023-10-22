using CorsairMessengerServer.Data.Entities;

namespace CorsairMessengerServer.Services.MessageBrokers
{
    public interface IMessageBroker
    {
        public Task SendMessageAsync(Message message);
    }
}
