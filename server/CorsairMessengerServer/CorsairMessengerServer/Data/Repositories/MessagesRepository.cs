using CorsairMessengerServer.Data.Entities.Message;

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
    }
}