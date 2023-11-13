using CorsairMessengerServer.Data;
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
        private readonly DataContext _context;

        public ContactsController(DataContext context)
        {
            _context = context;
        }

        [HttpGet("get")]
        public ActionResult<object[]> GetContacts([FromBody] ContactsListRequest request)
        {
            var userIdClaim = HttpContext.User.FindFirstValue(ClaimTypes.NameIdentifier)!;

            var userId = int.Parse(userIdClaim);

            var contactsIds = _context.Messages
                .Where(message => message.SenderId == userId)
                .Include(message => message.Receiver)
                .Distinct()
                .OrderBy(message => message.Id)
                .Skip(request.Offset)
                .Take(request.Count)
                .Select(message => new { message.Receiver!.Id, message.Receiver.Nickname })
                .ToArray();

            return Ok(contactsIds);
        }
    }
}
