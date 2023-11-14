using CorsairMessengerServer.Data.Repositories;
using CorsairMessengerServer.Models.Contacts;
using CorsairMessengerServer.Models.Messages;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Http;
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

        [HttpGet("pull")]
        public ActionResult<object[]> GetMessages([FromBody] MessagesPullRequest request)
        {
            var userIdClaim = HttpContext.User.FindFirstValue(ClaimTypes.NameIdentifier)!;

            var userId = int.Parse(userIdClaim);

            var messages = _messagesRepository.GetMessages(userId, request);

            return Ok(messages);
        }
    }
}
