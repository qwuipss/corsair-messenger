using CorsairMessengerServer.Data.Entities;

namespace CorsairMessengerServer.Models.Contacts
{
    public record ContactsListResponse(UserEntity[] Contacts);
}
