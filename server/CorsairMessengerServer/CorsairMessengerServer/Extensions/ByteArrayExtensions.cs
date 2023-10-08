using System.Text;

namespace CorsairMessengerServer.Extensions
{
    public static class ByteArrayExtensions
    {
        public static string Decode(this byte[] bytes, int count)
        {
            return Encoding.UTF8.GetString(bytes, 0, count);
        }
    }
}
