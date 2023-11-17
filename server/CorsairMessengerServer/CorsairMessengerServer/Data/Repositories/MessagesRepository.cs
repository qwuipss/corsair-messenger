using CorsairMessengerServer.Data.Entities;
using CorsairMessengerServer.Data.Entities.Request.Message;
using CorsairMessengerServer.Models.Messages;

namespace CorsairMessengerServer.Data.Repositories
{
    public class MessagesRepository
    {
        private readonly DataContext _context;

        public MessagesRepository(DataContext context)
        {
            _context = context;
        }

        public async Task AddMessageAsync(MessageEntity message)
        {
            await _context.Messages.AddAsync(message);

            await _context.SaveChangesAsync();
        }

        public MessageHistoryResponseEntity[] GetMessages(int userId, MessagesLoadRequest request)
        {
            return _context.Messages
                .Where(message =>
                   message.SenderId == userId && message.ReceiverId == request.UserId
                || message.SenderId == request.UserId && message.ReceiverId == userId)
                .Where(message => message.Id < request.MessageId)
                .OrderByDescending(message => message.Id)
                .Select(message => new MessageHistoryResponseEntity
                {
                    Id = message.Id,
                    SenderId = message.SenderId,
                    ReceiverId = message.ReceiverId,
                    Text = message.Text,
                    SendTime = message.SendTime,
                })
                .Take(request.Count)
                .ToArray();
        }
    }
}