import asyncio
import ssl
import websockets
import json
import requests
import urllib3
from .MessageSerializer import MessageSerializer
from threading import Thread
from websockets.sync.client import connect
from os.path import dirname, realpath, exists

class Client:

    SERVER_IP_ADDRESS_PORT = "127.0.0.1:8080"

    SERVER_URI = f"https://{SERVER_IP_ADDRESS_PORT}"

    SERVER_WEBSOCKET_CONNECT_URI = f"wss://{SERVER_IP_ADDRESS_PORT}"

    AUTH_TOKEN_LOAD_FILENAME = f"{dirname(realpath(__file__))}/auth.json"

    def __init__(self) -> None:
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.__unverified_ssl_context = ssl._create_unverified_context()

        load_info = Client.__try_load_auth_token()
        
        self.__authorized = auth_token_exists = load_info[0]
        self.__auth_token = load_info[1]

        if auth_token_exists:
            self.__check_auth_token_validity()
        
        if self.__authorized:

            headers = { "Authorization" : self.__auth_token }

            self.__websocket = connect(Client.SERVER_WEBSOCKET_CONNECT_URI, ssl_context=self.__unverified_ssl_context, additional_headers=headers)

    @staticmethod
    def __try_load_auth_token() -> tuple[bool, str]:
        
        if not exists(Client.AUTH_TOKEN_LOAD_FILENAME):
            return (False, "")

        with open(Client.AUTH_TOKEN_LOAD_FILENAME, "r") as file:
            loaded_file = json.load(file)

        auth_token = loaded_file.get("auth_token") or ""
        auth_token_exists = bool(auth_token)

        return (auth_token_exists, auth_token)

    async def start_receiving(self) -> None:

        while True:
            message = self.__websocket.recv()
            print(json.dumps(message))

    def send_message(self, **message) -> None:

        serialized_message = MessageSerializer().encode(message)

        self.__websocket.send(serialized_message)

    def auth(self, login: str, password: str) -> None:
        pass

    def __check_auth_token_validity(self) -> None:

        headers = { "Authorization" : self.__auth_token }

        validate_response = requests.get(f"{Client.SERVER_URI}/account/validate", headers=headers, verify=False)

        self.__authorized = validate_response.status_code == 200

# uri = "wss://127.0.0.1:8080"

# unverified_ssl_context = 

# # id = 3
# headers_1 = { "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjMiLCJleHAiOjE3MjgwNDkwOTksImlzcyI6IkNvcnNhaXJNZXNzZW5nZXJTZXJ2ZXIiLCJhdWQiOiJDb3JzYWlyTWVzc2VuZ2VyQ2xpZW50In0.OqR47IoaYXffyZGgHwuIvWL78HM3ovxktfHflt7heZA" }
# # id = 4
# headers_2 = { "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQiLCJleHAiOjE3MjgzNzY3NDQsImlzcyI6IkNvcnNhaXJNZXNzZW5nZXJTZXJ2ZXIiLCJhdWQiOiJDb3JzYWlyTWVzc2VuZ2VyQ2xpZW50In0.FZyVN2eUXKR05NJmv0dsbfkFaIH7UUA3lxmANqhj-cE" }


# async def client_1():

#     async with websockets.connect(uri, ssl=unverified_ssl_context, extra_headers=headers_1) as websocket:
#         while True:
#             print("client_1 working")
#             await websocket.send(json.dumps({ "recieverid" : 4, "text" : "hello world" }))
#             await asyncio.sleep(3)

# #str(base64.b64encode(b'hello world' * 1000)
# async def client_2():    
    
#     async with websockets.connect(uri, ssl=unverified_ssl_context, extra_headers=headers_2) as websocket:
#         while True:
#             print("client_2 working")
#             message = await websocket.recv()
#             print(json.dumps(message))

# async def main():

#     await asyncio.gather(client_1(), client_2())
#     #await asyncio.gather(client_2())
    

# if __name__ == '__main__':

#     loop = asyncio.get_event_loop()

#     try:
#         loop.run_until_complete(main())
#     finally:
#         loop.close()
