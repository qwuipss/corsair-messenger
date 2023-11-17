namespace CorsairMessengerServer.Models.Contacts.Search
{
    public record ContactsSearchRequest(string Pattern, int Count, int Offset);
}
