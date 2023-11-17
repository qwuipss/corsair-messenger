using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Data.Entities.Request.Message
{
    public abstract class MessageDeliveryBaseEntity
    {
        public enum MessageResponseEntityType
        {
            New = 0,
            Callback = 1,
        }

        [JsonPropertyName("type")]
        public int Type { get; set; }
    }
}
