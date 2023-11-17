using CorsairMessengerServer.Data.Entities.Api.User;

namespace CorsairMessengerServer.Models.Contacts
{
    public record ContactsListResponse(UserResponseEntity[] Contacts);
}
