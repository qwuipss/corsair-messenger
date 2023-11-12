using CorsairMessengerServer.Helpers;
using System.ComponentModel.DataAnnotations;
using static CorsairMessengerServer.Data.Constraints.UserEntityConstraints;

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

        public required string Password { get; set; }
    }
}
