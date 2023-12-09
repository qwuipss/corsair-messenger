using CorsairMessengerServer.Data.Constraints;
using CorsairMessengerServer.Helpers;
using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Auth
{
    public class AuthRequest
    {
        [JsonPropertyName("login")]
        public required string Login { get; set; }

        [JsonPropertyName("password")]
        [MinLength(UserEntityConstraints.NICKNAME_MIN_LENGTH)]
        [MaxLength(UserEntityConstraints.NICKNAME_MAX_LENGTH)]
        public required string Password { get; set; }
    }
}
