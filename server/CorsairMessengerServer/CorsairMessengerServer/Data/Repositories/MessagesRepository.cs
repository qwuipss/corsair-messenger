using CorsairMessengerServer.Data.Entities;
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

        /// <returns>
        ///     Array of anonymous objects { Id: int, Text: string, SendTime: DateTime }
        /// </returns>
        public object[] GetMessages(int userId, MessagesPullRequest request)
        {
            return _context.Messages
                .Where(message =>
                   message.SenderId == userId && message.ReceiverId == request.UserId
                || message.SenderId == request.UserId && message.ReceiverId == userId)
                .Where(message => message.Id > request.MessageId)
                .Select(message => new { message.Id, sender_id = message.SenderId, message.Text, send_time = message.SendTime })
                .OrderBy(message => message.Id)
                .Skip(request.Offset)
                .Take(request.Count)
                .ToArray();
        }
    }
}