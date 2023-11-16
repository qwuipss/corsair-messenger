using CorsairMessengerServer.Data.Entities;
using CorsairMessengerServer.Models.Contacts;
using CorsairMessengerServer.Models.Messages;
using Microsoft.EntityFrameworkCore;
using System.Diagnostics;
using System.Text.Json;

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