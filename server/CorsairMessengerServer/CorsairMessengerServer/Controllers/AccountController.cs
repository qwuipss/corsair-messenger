using CorsairMessengerServer.Data.Entities;
using CorsairMessengerServer.Data.Repositories.Users;
using CorsairMessengerServer.Extensions;
using CorsairMessengerServer.Helpers;
using CorsairMessengerServer.Models.Auth;
using CorsairMessengerServer.Models.Register;
using CorsairMessengerServer.Services.PasswordHasher;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using static CorsairMessengerServer.Data.Constraints.UserEntityConstraints;

namespace CorsairMessengerServer.Controllers
{
    [Authorize]
    [ApiController]
    [Route("account")]
    public class AccountController : ControllerBase
    {
        private const int AUTH_TOKEN_LIFETIME_MINUTES = 365 * 24 * 60;

        private readonly IUserRepository _userRepository;

        public AccountController(IUserRepository userRepository)
        {
            _userRepository = userRepository;
        }

        [AllowAnonymous]
        [HttpPost("login")]
        public async Task<ActionResult<AuthResponse>> Login([FromBody] AuthRequest request, [FromServices] IPasswordHasher hasher)
        {
            var user = await _userRepository.GetUserByLogin(request.Login, true);

            if (user is null)
            {
                return BadRequest(new { Field = "login" });
            }

            var verified = hasher.Verify(request.Password, user.Password);

            if (!verified)
            {
                return BadRequest(new { Field = "password" });
            }

            var token = GetAuthToken(user);

            var response = new AuthResponse(token);

            return Ok(response);
        }

        [AllowAnonymous]
        [HttpPost("register")]
        public async Task<ActionResult<AuthResponse>> Register([FromBody] RegisterRequest request, [FromServices] IPasswordHasher hasher)
        {
            var nickname = request.Nickname;

            if (!nickname.Length.InRange(NICKNAME_MIN_LENGTH, NICKNAME_MAX_LENGTH))
            {
                return BadRequest(new { Field = nameof(nickname) });
            }

            var email = request.Email;

            if (!RegexHelper.IsEmail(email))
            {
                return BadRequest(new { Field = nameof(email) });
            }

            var password = request.Password;

            if (!password.Length.InRange(PASSWORD_MIN_LENGTH, PASSWORD_MAX_LENGTH))
            {
                return BadRequest(new { Field = nameof(password) });
            }

            var isNicknameExist = await _userRepository.IsNicknameExist(nickname);

            if (isNicknameExist)
            {
                return Conflict(new { Field = nameof(nickname) });
            }

            var isEmailExist = await _userRepository.IsEmailExist(email);

            if (isEmailExist)
            {
                return Conflict(new { Field = nameof(nickname) });
            }

            var user = CreateUser(nickname, email, password, hasher);

            await _userRepository.AddUser(user);

            var token = GetAuthToken(user);

            var response = new AuthResponse(token);

            return Ok(response);
        }

        private static User CreateUser(string nickname, string email, string password, IPasswordHasher hasher)
        {
            var hashedPassword = hasher.Hash(password);

            return new User { Nickname = nickname, Email = email, Password = hashedPassword };
        }

        private static string GetAuthToken(User user)
        {
            var claims = new List<Claim> { new Claim(ClaimTypes.NameIdentifier, user.Id.ToString()) };

            var jwt = new JwtSecurityToken(
                    issuer: AuthOptions.ISSUER,
                    audience: AuthOptions.AUDIENCE,
                    claims: claims,
                    expires: DateTime.UtcNow.Add(TimeSpan.FromMinutes(AUTH_TOKEN_LIFETIME_MINUTES)),
                    signingCredentials: new SigningCredentials(AuthOptions.SymmetricSecurityKey, SecurityAlgorithms.HmacSha256));

            var token = new JwtSecurityTokenHandler().WriteToken(jwt);

            return token;
        }
    }
}
