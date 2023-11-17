using CorsairMessengerServer.Data.Entities.Request.Message;
using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Data.Entities.Response.Message
{
    public class MessageDeliveryCallbackEntity : MessageDeliveryBaseEntity
    {
        [JsonPropertyName("message_id")]
        public int Id { get; set; }

        [JsonPropertyName("user_id")]
        public int UserId { get; set; }

        [JsonPropertyName("text")]
        public string? Text { get; set; }

        [JsonPropertyName("send_time")]
        public DateTime SendTime { get; set; }
    }
}
