using CorsairMessengerServer.Data;
using CorsairMessengerServer.Data.Repositories;
using CorsairMessengerServer.Models.Contacts;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Security.Claims;

namespace CorsairMessengerServer.Controllers
{
    [Authorize]
    [Route("contacts")]
    [ApiController]
    public class ContactsController : ControllerBase
    {
        private readonly MessagesRepository _messagesRepository;

        public ContactsController(MessagesRepository messagesRepository)
        {
            _messagesRepository = messagesRepository;
        }

        [HttpGet("get")]
        public ActionResult<object[]> GetContacts([FromBody] ContactsListRequest request)
        {
            var userIdClaim = HttpContext.User.FindFirstValue(ClaimTypes.NameIdentifier)!;

            var userId = int.Parse(userIdClaim);

            var contacts = _messagesRepository.GetContacts(userId, request);

            return Ok(contacts);
        }
    }
}
