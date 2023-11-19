using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Contacts.List
{
    public class ContactsListRequest
    {
        private const int COUNT_MAX_VALUE = 100;

        private int _count;

        private int _offset;

        [JsonPropertyName("offset")]
        public int Offset 
        {
            get
            {
                return _offset;
            }
            set
            {
                if (value < 0)
                {
                    _offset = 0;
                }
                else
                {
                    _offset = value;
                }
            }
        }

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
