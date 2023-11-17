using CorsairMessengerServer.Data;
using CorsairMessengerServer.Data.Repositories;
using CorsairMessengerServer.Models.Contacts;
using CorsairMessengerServer.Models.Contacts.List;
using CorsairMessengerServer.Models.Contacts.Search;
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
        private readonly UsersRepository _usersRepository;

        public ContactsController(UsersRepository usersRepository)
        {
            _usersRepository = usersRepository;
        }

        [HttpGet("get")]
        public ActionResult<ContactsListResponse> GetContacts([FromBody] ContactsListRequest request)
        {
            var userIdClaim = HttpContext.User.FindFirstValue(ClaimTypes.NameIdentifier)!;

            var userId = int.Parse(userIdClaim);

            var contacts = _usersRepository.GetContacts(userId, request);

            return Ok(new ContactsListResponse(contacts));
        }

        [AllowAnonymous]
        [HttpPost("search")]
        public ActionResult<ContactsListResponse> SearchContacts([FromBody] ContactsSearchRequest request)
        {
            var contacts = _usersRepository.SearchContacts(request);

            return Ok(new ContactsListResponse(contacts));
        }
    }
}
