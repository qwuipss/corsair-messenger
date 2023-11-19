using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Contacts.Search
{
    public class ContactsSearchRequest
    {
        private const int COUNT_MAX_VALUE = 100;

        private int _count;

        [JsonPropertyName("pattern")]
        public required string Pattern { get; set; }

        [JsonPropertyName("count")]
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
    }
}
