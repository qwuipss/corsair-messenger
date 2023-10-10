using CorsairMessengerServer.Data.Constraints;
using CorsairMessengerServer.Data.Entities.Message;
using CorsairMessengerServer.Data.Repositories.WebSockets;
using CorsairMessengerServer.Extensions;
using CorsairMessengerServer.Services.MessageBrokers;
using Microsoft.AspNetCore.DataProtection;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Net.Sockets;
using System.Net.WebSockets;
using System.Text;
using System.Text.Json;

namespace CorsairMessengerServer.Managers
{
    public class WebSocketsManager
    {
        public record WebSocketConnection(int SocketId, WebSocket WebSocket);

        private readonly IWebSocketsRepository _webSocketsRepository;

        private readonly IMessageBroker _messageBroker;

        public WebSocketsManager(IWebSocketsRepository webSocketsRepository, IMessageBroker messageBroker)
        {
            _webSocketsRepository = webSocketsRepository;
            _messageBroker = messageBroker;
        }

        public WebSocketConnection OnConnected(int socketId, WebSocket webSocket)
        {
            var webSocketConnection = new WebSocketConnection(socketId, webSocket);

            _webSocketsRepository.AddWebSocket(socketId, webSocket);

            return webSocketConnection;
        }

        public void OnDisconnected(WebSocketConnection webSocketConnection)
        {
            _webSocketsRepository.RemoveWebSocket(webSocketConnection.SocketId);
        }

        public async Task StartReceiving(WebSocketConnection webSocketConnection)
        {
            var socketId = webSocketConnection.SocketId;
            var webSocket = webSocketConnection.WebSocket;

            var buffer = new byte[MessageEntityConstraints.MESSAGE_MAX_LENGTH * 2];
            var contentBuilder = new List<byte>();

            while (webSocket.State is WebSocketState.Open)
            {
                var receiveResult = await webSocket.ReceiveAsync(new ArraySegment<byte>(buffer), CancellationToken.None);

                if (receiveResult.MessageType is WebSocketMessageType.Text)
                {
                    if (ReceiveMessage(buffer, receiveResult, contentBuilder)
                     && TryParseMessageSendingRequest(contentBuilder.ToArray(), out var message))
                    {
                        PostInitMessage(message, socketId);

                        SendMessage(message);

                        contentBuilder.Clear();
                    }
                }
                else if (receiveResult.MessageType is WebSocketMessageType.Close)
                {
                    OnDisconnected(webSocketConnection);
                }
            }
        }

        private static bool ReceiveMessage(byte[] buffer, WebSocketReceiveResult receiveResult, List<byte> contentBuilder)
        {
            contentBuilder.ReceiveBytes(buffer, receiveResult);

            return receiveResult.EndOfMessage;
        }

        private static bool TryParseMessageSendingRequest(byte[] buffer, out Message request)
        {
            try
            {
                var options = new JsonSerializerOptions
                {
                    PropertyNameCaseInsensitive = true,
                };

                var memoryStream = new MemoryStream(buffer, 0, buffer.Length);

                request = (JsonSerializer.Deserialize(memoryStream, typeof(Message), options) as Message)!;
            }
            catch
            {
                request = null!;

                return false;
            }

            return true;
        }

        private static void PostInitMessage(Message message, int socketId)
        {
            message.SenderId = socketId;
            message.SendTime = DateTime.UtcNow;
        }

        private void SendMessage(Message message)
        {
            _messageBroker.DeliverMessage(message);
        }
    }
}
