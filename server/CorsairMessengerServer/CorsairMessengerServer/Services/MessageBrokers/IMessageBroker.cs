using CorsairMessengerServer.Data.Entities;
using CorsairMessengerServer.Data.Entities.Request;

namespace CorsairMessengerServer.Services.MessageBrokers
{
    public interface IMessageBroker
    {
        public Task SendMessageAsync(MessageEntity message);

        public Task SendMessageDeliveryCallbackIfPossibleAsync(MessageEntity message, MessageDeliveryRequestEntity deliveryRequestMessage);
    }
}
