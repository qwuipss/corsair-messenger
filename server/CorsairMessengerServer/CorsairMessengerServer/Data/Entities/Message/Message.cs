using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Data.Entities.Message
{
    public class Message
    {
        public int Id { get; set; }

        [JsonIgnore]
        public int SenderId { get; set; }

        public required int RecieverId { get; set; }

        public required string Text { get; set; }

        [JsonIgnore]
        public DateTime SendTime { get; set; }
    }
}
