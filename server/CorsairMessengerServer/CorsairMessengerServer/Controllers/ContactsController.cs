using CorsairMessengerServer.Data.Repositories;
using CorsairMessengerServer.Models.Contacts;
using CorsairMessengerServer.Models.Contacts.List;
using CorsairMessengerServer.Models.Contacts.Search;
using CorsairMessengerServer.Models.Contacts.Single;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
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

        [HttpGet("get-many")]
        public async Task<ActionResult<ContactsListResponse>> GetContactsAsync([FromBody] ContactsListRequest request)
        {
            var userIdClaim = HttpContext.User.FindFirstValue(ClaimTypes.NameIdentifier)!;

            var userId = int.Parse(userIdClaim);

            var contacts = await _usersRepository.GetContactsAsync(userId, request);

            var response = new ContactsListResponse
            {
                Contacts = contacts,
            };

            return Ok(response);
        }

        [HttpGet("get-single")]
        public async Task<ActionResult<ContactResponse>> GetContactsAsync([FromBody] ContactRequest request)
        {
            var contact = await _usersRepository.GetContactAsync(request.Id);

            if (contact is null)
            {
                return BadRequest(nameof(request.Id));
            }

            var response = new ContactResponse
            {
                Contact = contact,
            };

            return Ok(response);
        }

        [AllowAnonymous]
        [HttpPost("search")]
        public async Task<ActionResult<ContactsListResponse>> SearchContacts([FromBody] ContactsSearchRequest request)
        {
            var contacts = await _usersRepository.SearchContactsAsync(request);

            var response = new ContactsListResponse
            {
                Contacts = contacts,
            };

            return Ok(response);
        }
    }
}
