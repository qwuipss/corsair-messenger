using CorsairMessengerServer.Data.Entities;
using CorsairMessengerServer.Models.Contacts;
using Microsoft.EntityFrameworkCore;

namespace CorsairMessengerServer.Data.Repositories
{
    public class MessagesRepository
    {
        private readonly DataContext _context;

        public MessagesRepository(DataContext context)
        {
            _context = context;
        }

        public async Task AddMessageAsync(Message message)
        {
            await _context.Messages.AddAsync(message);

            await _context.SaveChangesAsync();
        }

        /// <returns>
        ///     Array of anonymous objects { Id: int, Nickname: string }
        /// </returns>
        public object[] GetContacts(int userId, ContactsListRequest request)
        {
            return _context.Messages
                .Where(message => message.SenderId == userId)
                .Include(message => message.Receiver)
                .Select(message => new { message.Receiver!.Id, message.Receiver.Nickname })
                .OrderBy(user => user.Id)
                .Distinct()
                .Skip(request.Offset)
                .Take(request.Count)
                .ToArray();
        }
    }
}