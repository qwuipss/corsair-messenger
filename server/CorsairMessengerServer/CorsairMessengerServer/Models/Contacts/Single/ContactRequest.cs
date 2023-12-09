using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Contacts.Single
{
    public class ContactRequest
    {
        [JsonPropertyName("id")]
        public required int Id { get; set; }
    }
}
