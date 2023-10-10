using CorsairMessengerServer.Managers;
using System.Security.Claims;

namespace CorsairMessengerServer.Middlewares
{
    public class WebSocketsConnectionsMiddleware
    {
        private readonly RequestDelegate _next;

        private readonly WebSocketsManager _webSocketsManager;

        public WebSocketsConnectionsMiddleware(RequestDelegate next, WebSocketsManager webSocketsManager)
        {
            _next = next;
            _webSocketsManager = webSocketsManager;
        }

        public async Task Invoke(HttpContext context)
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
                context.Response.StatusCode = StatusCodes.Status401Unauthorized;

                await context.Response.WriteAsJsonAsync(new { ErrorInfo = "invalid auth token" });

                return;
            }

            var webSocketConnection = _webSocketsManager.OnConnected(socketId, webSocket);

            await _webSocketsManager.StartReceiving(webSocketConnection);
        }
    }
}
