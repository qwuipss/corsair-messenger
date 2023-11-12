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
        
        self.__is_authorized = load_info[0]
        auth_token = load_info[1]

        if self.__is_authorized and Client.__check_auth_token_validity(auth_token):
            headers = { "Authorization" : auth_token }
            self.__websocket = connect(Client.SERVER_WEBSOCKET_CONNECT_URI, ssl_context=self.__unverified_ssl_context, additional_headers=headers)
        else:
            self.__websocket = None
            self.__is_authorized = False

    @property
    def is_authorized(self) -> bool:
        return self.__is_authorized

    @staticmethod
    def __try_load_auth_token() -> tuple[bool, str]:
        
        if not exists(Client.AUTH_TOKEN_LOAD_FILENAME):
            return (False, "")

        with open(Client.AUTH_TOKEN_LOAD_FILENAME, "r") as file:
            loaded_file = json.load(file)

        auth_token = loaded_file.get("auth_token") or ""

        return (bool(auth_token), auth_token)

    @staticmethod
    def __check_auth_token_validity(auth_token: str) -> bool:

        if not isinstance(auth_token, str):
            raise ValueError(auth_token)

        headers = { "Authorization" : auth_token }

        validate_response = requests.get(f"{Client.SERVER_URI}/account/validate", headers=headers, verify=False)

        return validate_response.status_code == 200
    
    def start_receiving(self) -> None:

        def start_receiving() -> None:

            while True:
                message = self.__websocket.recv()
                print(json.dumps(message))

        if not self.__is_authorized:
            raise ValueError(self.__is_authorized)
        
        Thread(target=start_receiving).start()

    def send_message(self, **message) -> None:

        if not self.__is_authorized:
            raise ValueError(self.__is_authorized)
        
        serialized_message = MessageSerializer().encode(message)

        self.__websocket.send(serialized_message)

    def auth(self, login: str, password: str) -> None:
        pass


# # id = 3
# headers_1 = { "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjMiLCJleHAiOjE3MjgwNDkwOTksImlzcyI6IkNvcnNhaXJNZXNzZW5nZXJTZXJ2ZXIiLCJhdWQiOiJDb3JzYWlyTWVzc2VuZ2VyQ2xpZW50In0.OqR47IoaYXffyZGgHwuIvWL78HM3ovxktfHflt7heZA" }
# # id = 4
# headers_2 = { "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQiLCJleHAiOjE3MjgzNzY3NDQsImlzcyI6IkNvcnNhaXJNZXNzZW5nZXJTZXJ2ZXIiLCJhdWQiOiJDb3JzYWlyTWVzc2VuZ2VyQ2xpZW50In0.FZyVN2eUXKR05NJmv0dsbfkFaIH7UUA3lxmANqhj-cE" }
