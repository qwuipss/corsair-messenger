using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Caching.Distributed;
using System.Security.Claims;

namespace CorsairMessengerServer.Middlewares
{
    public class SessionValidityCheckMiddleware
    {
        private readonly RequestDelegate _next;

        public SessionValidityCheckMiddleware(RequestDelegate next)
        {
            _next = next;
        }

        public async Task InvokeAsync(HttpContext context, [FromServices] IDistributedCache cache)
        {
            if (!context.Request.Headers.ContainsKey("Authorization"))
            {
                await _next.Invoke(context);

                return;
            }

            var userId = context.User.FindFirstValue(ClaimTypes.NameIdentifier);

            if (userId is null || !int.TryParse(userId, out _))
            {
                context.Response.Clear();

                context.Response.StatusCode = StatusCodes.Status401Unauthorized;

                return;
            }

            var sessionId = context.User.FindFirstValue(ClaimTypes.Sid);

            if (sessionId is null)
            {
                context.Response.Clear();

                context.Response.StatusCode = StatusCodes.Status401Unauthorized;

                return;
            }

            var cachedSessionId = await cache.GetStringAsync(userId);

            if (cachedSessionId != sessionId)
            {
                context.Response.Clear();

                context.Response.StatusCode = StatusCodes.Status401Unauthorized;

                return;
            }

            await _next.Invoke(context);
        }
    }
}
