using CorsairMessengerServer.Helpers;
using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;
using static CorsairMessengerServer.Data.Constraints.UserEntityConstraints;

namespace CorsairMessengerServer.Data.Entities
{
    public class UserEntity
    {
        public int Id { get; set; }

        [MinLength(NICKNAME_MIN_LENGTH)]
        [MaxLength(NICKNAME_MAX_LENGTH)]
        [RegularExpression(RegexHelper.NicknameValidationRegex)]
        public string? Nickname { get; set; }

        [RegularExpression(RegexHelper.EmailValidationRegex)]
        public string? Email { get; set; }

        [JsonIgnore]
        public string? Password { get; set; }
    }
}
