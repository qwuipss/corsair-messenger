using CorsairMessengerServer.Data.Entities.Api.User;
using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Contacts.Single
{
    public class ContactResponse
    {
        [JsonPropertyName("contact")]
        public required UserResponseEntity Contact { get; set; }
    }
}
