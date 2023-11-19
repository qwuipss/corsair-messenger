using CorsairMessengerServer.Data.Entities.Request.Message;
using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Messages
{
    public class MessagesListResponse
    {
        [JsonPropertyName("messages")]
        public required MessageHistoryResponseEntity[] Messages { get; set; }
    }
}
