using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Data.Entities.Api.User
{
    public class UserResponseEntity
    {
        [JsonPropertyName("user_id")]
        public int Id { get; set; }

        [JsonPropertyName("nickname")]
        public string? Nickname { get; set; }
    }
}
