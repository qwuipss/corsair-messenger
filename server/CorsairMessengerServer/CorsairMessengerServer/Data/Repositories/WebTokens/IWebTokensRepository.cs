using System.Net.WebSockets;

namespace CorsairMessengerServer.Data.Repositories.WebTokens
{
    public interface IWebTokensRepository
    {
        public void AddWebSocket(int userId, WebSocket webSocket);

        public Task RemoveWebSocket(int userId);
    }
}
