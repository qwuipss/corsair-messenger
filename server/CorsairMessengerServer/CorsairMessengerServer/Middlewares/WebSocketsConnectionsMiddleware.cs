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

            var userIdClaim = context.User.FindFirstValue(ClaimTypes.NameIdentifier)!;

            var socketId = int.Parse(userIdClaim);

            var webSocketConnection = webSocketsManager.OnConnected(socketId, webSocket);

            await webSocketsManager.StartReceivingAsync(webSocketConnection);
        }
    }
}
