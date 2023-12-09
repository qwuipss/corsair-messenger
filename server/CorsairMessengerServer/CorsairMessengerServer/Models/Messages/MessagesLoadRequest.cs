using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Messages
{
    public class MessagesLoadRequest
    {
        private int _messageId;

        [JsonPropertyName("user_id")]
        public required int UserId { get; set; }

        [JsonPropertyName("message_id")]
        public required int MessageId
        {
            get
            {
                return _messageId;
            }
            set
            {
                if (value < 0)
                {
                    _messageId = int.MaxValue;
                }
                else
                {
                    _messageId = value;
                }
            }
        }

        [JsonPropertyName("count")]
        [Range(0, 100)]
        public required int Count { get; set; }
    }
}
