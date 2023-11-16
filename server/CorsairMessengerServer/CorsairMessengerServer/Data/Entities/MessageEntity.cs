using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Data.Entities
{
    public class MessageEntity
    {
        public int Id { get; set; }

        [JsonIgnore]
        public int SenderId { get; set; }

        [JsonPropertyName("receiver_id")]
        public int ReceiverId { get; set; }

        [JsonIgnore]
        public UserEntity? Receiver { get; set; }

        [JsonPropertyName("text")]
        public string? Text { get; set; }

        [JsonIgnore]
        public DateTime SendTime { get; set; }
    }
}
