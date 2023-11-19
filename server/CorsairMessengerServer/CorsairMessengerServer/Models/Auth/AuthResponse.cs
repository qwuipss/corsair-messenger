using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Auth
{
    public class AuthResponse
    {
        [JsonPropertyName("token")]
        public required string Token { get; set; }
    }
}
