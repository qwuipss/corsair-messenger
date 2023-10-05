using CorsairMessengerServer.Data.Entities;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Concurrent;
using System.Net.WebSockets;

namespace CorsairMessengerServer.Data.Repositories.WebTokens
{
    public class WebTokensRepository : IWebTokensRepository
    {
        private static readonly ConcurrentDictionary<int, WebSocket> _connectedWebSockets;

        static WebTokensRepository()
        {
            _connectedWebSockets = new ConcurrentDictionary<int, WebSocket>();
        }

        public void AddWebSocket(int userId, WebSocket webSocket)
        {
            _connectedWebSockets[userId] = webSocket;
        }

        public async Task RemoveWebSocket(int userId)
        {
            if (_connectedWebSockets.TryRemove(userId, out var webSocket))
            {
                await webSocket.CloseAsync(WebSocketCloseStatus.NormalClosure, "Web socket close requested", CancellationToken.None);
            }
        }
    }
}
