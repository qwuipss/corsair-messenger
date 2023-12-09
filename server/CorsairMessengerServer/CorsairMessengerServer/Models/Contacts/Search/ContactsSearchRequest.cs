using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Contacts.Search
{
    public class ContactsSearchRequest
    {
        [JsonPropertyName("pattern")]
        public required string Pattern { get; set; }

        [JsonPropertyName("count")]
        [Range(0, 100)]
        public required int Count { get; set; }
    }
}
