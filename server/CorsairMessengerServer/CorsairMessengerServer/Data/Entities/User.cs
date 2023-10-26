using static CorsairMessengerServer.Data.Constraints.UserEntityConstraints;
using System.ComponentModel.DataAnnotations;
using CorsairMessengerServer.Helpers;

namespace CorsairMessengerServer.Data.Entities
{
    public class User
    {
        public int Id { get; set; }

        [MinLength(NICKNAME_MIN_LENGTH)]
        [MaxLength(NICKNAME_MAX_LENGTH)]
        [RegularExpression(RegexHelper.NicknameValidationRegex)]
        public required string Nickname { get; set; }

        [RegularExpression(RegexHelper.EmailValidationRegex)]
        public required string Email { get; set; }

        [MinLength(PASSWORD_MIN_LENGTH)]
        [MaxLength(PASSWORD_MAX_LENGTH)]
        public required string Password { get; set; }
    }
}
