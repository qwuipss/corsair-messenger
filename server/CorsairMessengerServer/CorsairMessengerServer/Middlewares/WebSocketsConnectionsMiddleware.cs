using CorsairMessengerServer.Managers;
using System.Security.Claims;

namespace CorsairMessengerServer.Middlewares
{
    public class WebSocketsConnectionsMiddleware
    {
        private readonly RequestDelegate _next;

        public WebSocketsConnectionsMiddleware(RequestDelegate next)
        {
            _next = next;
        }

        public async Task InvokeAsync(HttpContext context, WebSocketsManager webSocketsManager)
        {
            if (!context.WebSockets.IsWebSocketRequest)
            {
                await _next(context);

                return;
            }

            var webSocket = await context.WebSockets.AcceptWebSocketAsync();

            var userId = context.User.FindFirstValue(ClaimTypes.NameIdentifier);

            if (userId is null || !int.TryParse(userId, out var socketId))
            {
                return;
            }

            var webSocketConnection = webSocketsManager.OnConnected(socketId, webSocket);

            await webSocketsManager.StartReceivingAsync(webSocketConnection);
        }
    }
}
