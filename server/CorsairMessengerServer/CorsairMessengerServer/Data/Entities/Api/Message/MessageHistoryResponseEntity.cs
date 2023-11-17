using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Data.Entities.Request.Message
{
    public class MessageHistoryResponseEntity : MessageDeliveryBaseEntity
    {
        [JsonPropertyName("message_id")]
        public int Id { get; set; }

        [JsonPropertyName("sender_id")]
        public int SenderId { get; set; }

        [JsonPropertyName("receiver_id")]
        public int ReceiverId { get; set; }

        [JsonPropertyName("text")]
        public string? Text { get; set; }

        [JsonPropertyName("send_time")]
        public DateTime SendTime { get; set; }
    }
}
