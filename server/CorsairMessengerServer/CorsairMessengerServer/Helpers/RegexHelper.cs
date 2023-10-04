using System.Text.RegularExpressions;

namespace CorsairMessengerServer.Helpers
{
    public static partial class RegexHelper
    {
        public static bool IsEmail(string input)
        {
            return EmailRegex().IsMatch(input);
        }

        [GeneratedRegex("^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$")]
        private static partial Regex EmailRegex();
    }
}
