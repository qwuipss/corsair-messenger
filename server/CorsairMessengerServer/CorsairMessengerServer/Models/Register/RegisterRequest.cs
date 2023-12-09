using CorsairMessengerServer.Data.Constraints;
using CorsairMessengerServer.Helpers;
using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Models.Register
{
    public class RegisterRequest
    {
        [JsonPropertyName("email")]
        [RegularExpression(RegexHelper.EmailValidationRegex)]
        public required string Email { get; set; }

        [JsonPropertyName("nickname")]
        [RegularExpression(RegexHelper.NicknameValidationRegex)]
        [MinLength(UserEntityConstraints.NICKNAME_MIN_LENGTH)]
        [MaxLength(UserEntityConstraints.NICKNAME_MAX_LENGTH)]
        public required string Nickname { get; set; }


        [JsonPropertyName("password")]
        [MinLength(UserEntityConstraints.NICKNAME_MIN_LENGTH)]
        [MaxLength(UserEntityConstraints.NICKNAME_MAX_LENGTH)]
        public required string Password { get; set; }
    }
}
