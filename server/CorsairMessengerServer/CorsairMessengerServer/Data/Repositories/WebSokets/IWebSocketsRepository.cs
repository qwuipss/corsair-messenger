using System.Net.WebSockets;

namespace CorsairMessengerServer.Data.Repositories.WebSockets
{
    public interface IWebSocketsRepository
    {
        public void AddWebSocket(int userId, WebSocket webSocket);

        public Task RemoveWebSocket(int userId);

        public bool TryGetWebSocket(int socketId, out WebSocket webSocket);
    }
}
