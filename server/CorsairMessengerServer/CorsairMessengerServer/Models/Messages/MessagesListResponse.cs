using CorsairMessengerServer.Data.Entities.Request.Message;

namespace CorsairMessengerServer.Models.Messages
{
    public record MessagesListResponse(MessageHistoryResponseEntity[] Messages);
}
