using CorsairMessengerServer.Data.Constraints;
using CorsairMessengerServer.Data.Repositories.WebTokens;
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
    public class WebTokensManager
    {
        private class WebTokenHandler
        {
            private readonly int _socketId;

            private readonly WebSocket _webSocket;

            private readonly IMessageBroker _messageBroker;

            private string _decodedMessage;

            public WebTokenHandler(int socketId, WebSocket webSocket, IMessageBroker messageBroker) 
            {
                _socketId = socketId;
                _webSocket = webSocket;
                _messageBroker = messageBroker;
                _decodedMessage = string.Empty;
            }

            public async Task StartReceiving(WebSocket socket, WebSocketReceiveResult result, byte[] buffer)
            {
                _decodedMessage += Encoding.UTF8.GetString(buffer, 0, result.Count);

                if (result.EndOfMessage)
                {
                    _decodedMessage = string.Empty;
                }

                //while (_webSocket.State is WebSocketState.Open)
                //{


                //var receiveResult = await _webSocket.ReceiveAsync(new ArraySegment<byte>(buffer), CancellationToken.None);

                //if (receiveResult.MessageType is WebSocketMessageType.Close)
                //{
                //    onDisconnected.Invoke(_socketId);

                //    return;
                //}

                //if (receiveResult.MessageType is not WebSocketMessageType.Text)
                //{
                //    return;
                //}

                //_decodedMessage += buffer.GetUtf8String(receiveResult.Count);

                //if (!receiveResult.EndOfMessage)
                //{
                //    continue;
                //}

                //MessageSendingRequest? request;

                //try
                //{
                //    request = JsonSerializer.Deserialize<MessageSendingRequest>(_decodedMessage, new JsonSerializerOptions
                //    {
                //        PropertyNameCaseInsensitive = true,
                //    });
                //}
                //finally
                //{
                //    _decodedMessage = string.Empty;
                //}

                //if (request is not null)
                //{
                //    _messageBroker.Send(request);
                //}
                //}
            }
        }

        private readonly IWebTokensRepository _webTokensRepository;
        
        private readonly IMessageBroker _messageBroker;

        public WebTokensManager(IWebTokensRepository webTokensRepository, IMessageBroker messageBroker)
        {
            _webTokensRepository = webTokensRepository;
            _messageBroker = messageBroker;
        }

        public void OnConnected(int socketId, WebSocket webSocket)
        {
            _webTokensRepository.AddWebSocket(socketId, webSocket);
        }

        public void OnDisconnected(int socketId)
        {
            _webTokensRepository.RemoveWebSocket(socketId);
        }

        public async Task StartReceiving(int socketId, WebSocket webSocket)
        {

            var webSocketHandler = new WebTokenHandler(socketId, webSocket, _messageBroker);

            var buffer = new byte[MessageEntityConstraints.MESSAGE_MAX_LENGTH * 2];

            while (webSocket.State == WebSocketState.Open)
            {
                var result = await webSocket.ReceiveAsync(buffer: new ArraySegment<byte>(buffer),
                                                       cancellationToken: CancellationToken.None);

                if (result.MessageType == WebSocketMessageType.Text)
                {
                    await webSocketHandler.StartReceiving(webSocket, result, buffer);
                    return;
                }
                else if (result.MessageType == WebSocketMessageType.Close)
                {
                    OnDisconnected(socketId);
                    return;
                }

            }

        }
    }
}
