namespace CorsairMessengerServer.Models.Message
{
    public class MessageSendingRequest
    {
        public required int RecieverId { get; set; }

        public required int SenderId { get; set; }

        public required string Content { get; set; }
    }
}
