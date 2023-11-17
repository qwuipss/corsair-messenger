using CorsairMessengerServer.Data.Entities;
using CorsairMessengerServer.Data.Entities.Api.User;
using CorsairMessengerServer.Models.Contacts.List;
using CorsairMessengerServer.Models.Contacts.Search;
using Microsoft.EntityFrameworkCore;

namespace CorsairMessengerServer.Data.Repositories
{
    public class UsersRepository
    {
        private readonly DataContext _context;

        public UsersRepository(DataContext context)
        {
            _context = context;
        }

        public async Task<UserEntity?> GetUserByLoginAsync(string login, bool asNoTracking = false)
        {
            var query = _context.Users.Where(user => user.Email == login || user.Nickname == login);

            if (asNoTracking)
            {
                query.AsNoTracking();
            }

            var user = await query.SingleOrDefaultAsync();

            return user;
        }

        public async Task AddUserAsync(UserEntity user)
        {
            await _context.AddAsync(user);

            await _context.SaveChangesAsync();
        }

        public async Task<bool> IsNicknameExistAsync(string nickname)
        {
            var result = await _context.Users.AnyAsync(user => user.Nickname == nickname);

            return result;
        }

        public async Task<bool> IsEmailExistAsync(string email)
        {
            var result = await _context.Users.AnyAsync(user => user.Email == email);

            return result;
        }

        public async Task<bool> IsUserExist(int id)
        {
            var result = await _context.Users.AnyAsync(user => user.Id == id);

            return result;
        }

        public UserResponseEntity[] GetContacts(int userId, ContactsListRequest request)
        {
            return _context.Messages
                .Where(message => message.SenderId == userId)
                .Include(message => message.Receiver)
                .Select(message => new UserResponseEntity { Id = message.Receiver!.Id, Nickname = message.Receiver.Nickname })
                .Distinct()
                .OrderBy(user => user.Id)
                .Skip(request.Offset)
                .Take(request.Count)
                .ToArray();
        }

        public UserResponseEntity[] SearchContacts(ContactsSearchRequest request)
        {
            return _context.Users
                .Where(user => EF.Functions.Like(user.Nickname!, $"%{request.Pattern}%"))
                .Select(user => new UserResponseEntity { Id = user.Id, Nickname = user.Nickname })
                .OrderBy(user => user.Id)
                .Skip(request.Offset)
                .Take(request.Count)
                .ToArray();
        }
    }
}
