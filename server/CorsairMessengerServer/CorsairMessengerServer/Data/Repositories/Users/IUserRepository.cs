using CorsairMessengerServer.Data.Entities;
using Microsoft.EntityFrameworkCore;

namespace CorsairMessengerServer.Data.Repositories.Users
{
    public interface IUserRepository
    {
        public Task<User?> GetUserByLogin(string login, bool asNoTracking = false);

        public Task AddUser(User user);

        public Task<bool> IsNicknameExist(string nickname);

        public Task<bool> IsEmailExist(string email);
    }
}
