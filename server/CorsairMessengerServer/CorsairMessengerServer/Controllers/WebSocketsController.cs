using CorsairMessengerServer.Data.Constraints;
using CorsairMessengerServer.Data.Repositories.WebTokens;
using CorsairMessengerServer.Models.Message;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Http.HttpResults;
using Microsoft.AspNetCore.Mvc;
using System.Net.WebSockets;
using System.Runtime.Serialization.Json;
using System.Security.Claims;
using System.Text;
using System.Text.Json;

namespace CorsairMessengerServer.Controllers
{
    [Authorize]
    [ApiController]
    [Route("sockets")]
    public class WebSocketsController : ControllerBase
    {
        private readonly IWebTokensRepository _webTokensRepository;
        
        public WebSocketsController(IWebTokensRepository webTokensRepository) 
        { 
            _webTokensRepository = webTokensRepository;
        }

        [HttpGet("connect")]
        public async Task<IActionResult> ConnectWebSocket()
        {
            if (!HttpContext.WebSockets.IsWebSocketRequest)
            {
                return BadRequest(new { Error = "not a websocket connection request" });
            }

            var webSocket = await HttpContext.WebSockets.AcceptWebSocketAsync();
            
            var userId = HttpContext.User.FindFirstValue(ClaimTypes.NameIdentifier);

            if (userId is null || int.TryParse(userId, out var socketId))
            {
                return new UnauthorizedResult();
            }

            _webTokensRepository.AddWebSocket(socketId, webSocket);


            // add socket to redis
            // start listen socket
            // if socket sending data resend to reciever

            return Ok();
        }
    }
}
