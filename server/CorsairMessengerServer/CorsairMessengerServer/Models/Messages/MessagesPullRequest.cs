using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Messages
{
    public record MessagesPullRequest(int Count, int Offset)
    {
        [JsonPropertyName("user_id")]
        public int UserId { get; set; }
        
        [JsonPropertyName("message_id")]
        public int MessageId { get; set; }
    }
}
