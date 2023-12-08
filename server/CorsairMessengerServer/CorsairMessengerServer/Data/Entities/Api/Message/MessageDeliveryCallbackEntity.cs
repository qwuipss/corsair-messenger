using CorsairMessengerServer.Data.Entities.Request.Message;
using System.Text.Json.Serialization;

namespace CorsairMessengerServer.Data.Entities.Response.Message
{
    public class MessageDeliveryCallbackEntity : MessageDeliveryBaseEntity
    {
        [JsonPropertyName("message_id")]
        public int Id { get; set; }        
        
        [JsonPropertyName("local_message_id")]
        public int LocalId { get; set; }

        [JsonPropertyName("send_time")]
        public DateTime SendTime { get; set; }
    }
}
