namespace CorsairMessengerServer.Managers
{
    public class SessionManager
    {
        public static string GetSessionString(string userId, string sessionId)
        {
            return $"{userId}:{sessionId}";
        }
    }
}
