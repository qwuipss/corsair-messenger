using CorsairMessengerServer.Data.Repositories;
using CorsairMessengerServer.Models.Messages;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System.Security.Claims;

namespace CorsairMessengerServer.Controllers
{
    [Authorize]
    [Route("messages")]
    [ApiController]
    public class MessagesController : ControllerBase
    {
        private readonly MessagesRepository _messagesRepository;

        public MessagesController(MessagesRepository messagesRepository)
        {
            _messagesRepository = messagesRepository;
        }

        [HttpGet("load")]
        public ActionResult<MessagesListResponse> GetMessages([FromBody] MessagesLoadRequest request)
        {
            var userIdClaim = HttpContext.User.FindFirstValue(ClaimTypes.NameIdentifier)!;

            var userId = int.Parse(userIdClaim);

            var messages = _messagesRepository.GetMessages(userId, request);

            return Ok(messages);
        }
    }
}
