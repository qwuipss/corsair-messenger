using CorsairMessengerServer.Data.Constraints;
using CorsairMessengerServer.Data.Repositories.WebSockets;
using CorsairMessengerServer.Extensions;
using CorsairMessengerServer.Models.Message;
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
            var contentBuilder = new StringBuilder();

            while (webSocket.State is WebSocketState.Open)
            {
                var receiveResult = await webSocket.ReceiveAsync(new ArraySegment<byte>(buffer), CancellationToken.None);

                if (receiveResult.MessageType is WebSocketMessageType.Text)
                {
                    if (ReceiveMessage(buffer, receiveResult, contentBuilder) 
                     && TryParseMessageSendingRequest(contentBuilder.ToString(), out var request))
                    {
                        SendMessage(socketId, request);

                        contentBuilder.Clear();
                    }
                }
                else if (receiveResult.MessageType is WebSocketMessageType.Close)
                {
                    OnDisconnected(webSocketConnection);
                }
            }
        }

        private static bool ReceiveMessage(byte[] buffer, WebSocketReceiveResult receiveResult, StringBuilder contentBuilder)
        {
            var content = buffer.Decode(receiveResult.Count);

            contentBuilder.Append(content);

            return receiveResult.EndOfMessage;
        }

        private static bool TryParseMessageSendingRequest(string content, out MessageSendingRequest request)
        {
            try
            {
                request = JsonSerializer.Deserialize<MessageSendingRequest>(content, new JsonSerializerOptions
                {
                    PropertyNameCaseInsensitive = true,
                })!;
            }
            catch
            {
                request = null!;

                return false;
            }

            return true;
        }

        private void SendMessage(int senderId, MessageSendingRequest request)
        {
            request.SenderId = senderId;

            _messageBroker.DeliverMessage(request);
        }
    }
}
