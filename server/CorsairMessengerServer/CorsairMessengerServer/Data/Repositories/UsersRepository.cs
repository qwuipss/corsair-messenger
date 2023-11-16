using CorsairMessengerServer.Data.Entities;
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
    }
}
