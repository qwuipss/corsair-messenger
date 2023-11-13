using CorsairMessengerServer.Managers;
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

            var userIdClaim = context.User.FindFirstValue(ClaimTypes.NameIdentifier);

            if (userIdClaim is null || !int.TryParse(userIdClaim, out _))
            {
                context.Response.Clear();

                context.Response.StatusCode = StatusCodes.Status401Unauthorized;

                return;
            }

            var sessionIdClaim = context.User.FindFirstValue(ClaimTypes.Sid);

            if (sessionIdClaim is null)
            {
                context.Response.Clear();

                context.Response.StatusCode = StatusCodes.Status401Unauthorized;

                return;
            }

            var sessionString = SessionManager.GetSessionString(userIdClaim, sessionIdClaim);

            if (await cache.GetStringAsync(sessionString) is null)
            {
                context.Response.Clear();

                context.Response.StatusCode = StatusCodes.Status401Unauthorized;

                return;
            }

            await _next.Invoke(context);
        }
    }
}
