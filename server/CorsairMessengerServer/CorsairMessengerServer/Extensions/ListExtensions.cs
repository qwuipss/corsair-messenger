using System.Net.WebSockets;

namespace CorsairMessengerServer.Extensions
{
    public static class ListExtensions
    {
        public static void ReceiveBytes(this List<byte> list, byte[] buffer, WebSocketReceiveResult receiveResult)
        {
            for (int i = 0; i < receiveResult.Count; i++)
            {
                list.Add(buffer[i]);
            }
        }
    }
}
