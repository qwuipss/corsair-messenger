using CorsairMessengerServer.Data.Entities;
using Microsoft.EntityFrameworkCore;

namespace CorsairMessengerServer.Data.Repositories.Users
{
    public class UserRepository : IUserRepository
    {
        private readonly DataContext _context;

        public UserRepository(DataContext context)
        {
            _context = context;
        }

        public async Task<User?> GetUserByLogin(string login, bool asNoTracking = false)
        {
            var query = _context.Users
                .Where(user => user.Email == login || user.Nickname == login);

            if (asNoTracking)
            {
                query.AsNoTracking();
            }

            var user = await query.SingleOrDefaultAsync();

            return user;
        }

        public async Task AddUser(User user)
        {
            await _context.AddAsync(user);
            await _context.SaveChangesAsync();
        }

        public async Task<bool> IsNicknameExist(string nickname)
        {
            var result = await _context.Users.AnyAsync(user => user.Nickname == nickname);

            return result;
        }

        public async Task<bool> IsEmailExist(string email)
        {
            var result = await _context.Users.AnyAsync(user => user.Email == email);

            return result;
        }
    }
}
