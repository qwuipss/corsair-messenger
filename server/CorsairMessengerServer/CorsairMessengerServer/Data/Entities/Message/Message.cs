using System.Net.WebSockets;
using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Data.Entities.Message
{
    public class Message
    {
        [JsonIgnore]
        public int SenderId { get; set; }

        public required int RecieverId { get; set; }

        public required byte[] Content { get; set; }

        [JsonIgnore]
        public DateTime SendTime { get; set; }

        [JsonIgnore] // TEMP
        public MessageType MessageType { get; set; }
    }
}
