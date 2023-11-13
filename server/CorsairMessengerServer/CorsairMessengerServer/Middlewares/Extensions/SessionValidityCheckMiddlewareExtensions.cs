namespace CorsairMessengerServer.Middlewares.Extensions
{
    public static class SessionValidityCheckMiddlewareExtensions
    {
        public static IApplicationBuilder UseSessionValidityCheck(this IApplicationBuilder app)
        {
            if (app is null)
            {
                throw new ArgumentNullException(nameof(app));
            }

            return app.UseMiddleware<SessionValidityCheckMiddleware>();
        }
    }
}
