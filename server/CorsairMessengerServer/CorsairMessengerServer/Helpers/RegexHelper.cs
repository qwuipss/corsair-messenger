using System.Text.RegularExpressions;

namespace CorsairMessengerServer.Helpers
{
    public static partial class RegexHelper
    {
        public const string NicknameValidationRegex = "^[a-zA-Z0-9_]*$";

        public const string EmailValidationRegex = "^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,5}$";

        public static bool IsNickname(string input)
        {
            return NicknameRegex().IsMatch(input);
        }

        public static bool IsEmail(string input)
        {
            return EmailRegex().IsMatch(input);
        }

        [GeneratedRegex(NicknameValidationRegex)]
        private static partial Regex NicknameRegex();

        [GeneratedRegex(EmailValidationRegex)]
        private static partial Regex EmailRegex();
    }
}
