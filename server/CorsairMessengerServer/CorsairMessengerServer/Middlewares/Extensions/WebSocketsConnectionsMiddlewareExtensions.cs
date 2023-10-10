namespace CorsairMessengerServer.Middlewares.Extensions
{
    public static class WebSocketsConnectionsMiddlewareExtensions
    {
        public static IApplicationBuilder UseWebSocketsConnections(this IApplicationBuilder app)
        {
            if (app is null)
            {
                throw new ArgumentNullException(nameof(app));
            }

            return app.UseMiddleware<WebSocketsConnectionsMiddleware>();
        }
    }
}
