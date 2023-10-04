using Microsoft.IdentityModel.Tokens;
using System.Text;

namespace CorsairMessengerServer
{
    public static class AuthOptions
    {
        public const string ISSUER = "CorsairMessengerServer";

        public const string AUDIENCE = "CorsairMessengerClient";

        private const string KEY = "DevelopmentSecurityKey";

        public static readonly SymmetricSecurityKey SymmetricSecurityKey = new(Encoding.UTF8.GetBytes(KEY));
    }
}
