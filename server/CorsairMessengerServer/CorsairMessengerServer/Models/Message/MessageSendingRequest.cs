using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Message
{
    public class MessageSendingRequest
    {
        [JsonIgnore]
        public int SenderId { get; set; }

        public required int RecieverId { get; set; }

        public required string Content { get; set; }
    }
}
