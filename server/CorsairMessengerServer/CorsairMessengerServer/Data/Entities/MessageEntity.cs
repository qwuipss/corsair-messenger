namespace CorsairMessengerServer.Data.Entities
{
    public class MessageEntity
    {
        public int Id { get; set; }

        public int SenderId { get; set; }

        public int ReceiverId { get; set; }

        public UserEntity? Receiver { get; set; }

        public string? Text { get; set; }

        public DateTime SendTime { get; set; }
    }
}
