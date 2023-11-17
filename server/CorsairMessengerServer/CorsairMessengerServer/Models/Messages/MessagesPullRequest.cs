using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Messages
{
    public record MessagesPullRequest(int Offset)
    {
        private const int COUNT_MAX_VALUE = 100;

        private int _count;

        public int Count
        {
            get
            {
                return _count;
            }

            set
            {
                if (value < 0)
                {
                    _count = 0;
                }
                else if (value > COUNT_MAX_VALUE)
                {
                    _count = COUNT_MAX_VALUE;
                }
                else
                {
                    _count = value;
                }
            }
        }

        [JsonPropertyName("user_id")]
        public int UserId { get; set; }

        [JsonPropertyName("message_id")]
        public int MessageId { get; set; }
    }
}
