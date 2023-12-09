using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Contacts.List
{
    public class ContactsListRequest
    {
        [JsonPropertyName("offset")]
        [Range(0, int.MaxValue)]
        public required int Offset {  get; set; }

        [JsonPropertyName("count")]
        [Range(0, 100)]
        public required int Count { get; set; }
    }
}
