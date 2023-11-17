import ssl
import json
import requests
import urllib3
from SharedConstants import SECOND_WINDOW
from .MessageSerializer import MessageSerializer
from websockets.sync.client import connect
from os.path import dirname, realpath, exists

class Client:

    SERVER_IP_ADDRESS_PORT = "192.168.0.106:8080"

    SERVER_URI = f"https://{SERVER_IP_ADDRESS_PORT}"

    SERVER_WEBSOCKET_CONNECT_URI = f"wss://{SERVER_IP_ADDRESS_PORT}"

    AUTH_TOKEN_LOAD_FILENAME = f"{dirname(realpath(__file__))}/auth.json"

    if SECOND_WINDOW:
        SECOND_WINDOW_AUTH_TOKEN_LOAD_FILENAME = f"{dirname(realpath(__file__))}/authSecondWindow.json"
        __first_auth = True

    def __init__(self) -> None:
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.__unverified_ssl_context = ssl._create_unverified_context()

        load_info = Client.__try_load_auth_token()

        self.__is_authorized = load_info[0]
        self.__auth_token = load_info[1]

        if self.__is_authorized and self.__check_auth_token_validity():
            self.__connect_websocket()
        else:
            self.__websocket = None
            self.__is_authorized = False

    def __enter__(self) -> 'Client':
        return self

    def __exit__(self, *_) -> bool:

        self.__websocket.close()

        return True

    @property
    def is_authorized(self) -> bool:
        return self.__is_authorized

    @staticmethod
    def __try_load_auth_token() -> tuple[bool, str]:

        if SECOND_WINDOW and not Client.__first_auth:

            if not exists(Client.SECOND_WINDOW_AUTH_TOKEN_LOAD_FILENAME):
                return (False, "")
            
            with open(Client.SECOND_WINDOW_AUTH_TOKEN_LOAD_FILENAME, "r") as file:
                try:
                    loaded_file = json.load(file)
                except:
                    pass

        else:

            if not exists(Client.AUTH_TOKEN_LOAD_FILENAME):
                return (False, "")

            with open(Client.AUTH_TOKEN_LOAD_FILENAME, "r") as file:
                try:
                    loaded_file = json.load(file)
                    Client.__first_auth = False
                except:
                    pass

        auth_token = loaded_file.get("token") or ""

        return (bool(auth_token), auth_token)

    @staticmethod
    def __save_auth_token(auth_token: str) -> None:

        if not isinstance(auth_token, str):
            raise ValueError(auth_token)
        
        data = { "token" : auth_token }

        if SECOND_WINDOW and not Client.__first_auth:
            with open(Client.SECOND_WINDOW_AUTH_TOKEN_LOAD_FILENAME, "w") as file:
                file.write(json.dumps(data))
        else:
            with open(Client.AUTH_TOKEN_LOAD_FILENAME, "w") as file:
                file.write(json.dumps(data))

    def receive_message(self) -> None:

        if not self.__is_authorized:
            raise ValueError(self.__is_authorized)

        message = self.__websocket.recv()
        
        return message

    def send_message(self, **message) -> None:

        if not self.__is_authorized:
            raise ValueError(self.__is_authorized)
        
        serialized_message = MessageSerializer().encode(message)

        self.__websocket.send(serialized_message)

    def auth(self, login: str, password: str) -> bool:
        
        if not isinstance(login, str):
            raise ValueError(login)
        
        if not isinstance(password, str):
            raise ValueError(password)

        auth_response = requests.post(f"{Client.SERVER_URI}/account/login", json={ "login" : login, "password" : password }, verify=False)

        if auth_response.status_code == 200:

            self.__auth_token = "Bearer " + auth_response.json()["token"]

            self.__connect_websocket()
            self.__save_auth_token(self.__auth_token)

            Client.__first_auth = False

            return True
        
        return False

    def get_contacts(self) -> dict:
        
        headers = { "Authorization" : self.__auth_token }

        response = requests.get(f"{Client.SERVER_URI}/contacts/get", headers=headers, json={ "offset" : 0, "count" : 50 }, verify=False)

        return response.json()["contacts"]

    def search_contacts(self, text) -> dict:

        headers = { "Authorization" : self.__auth_token }

        response = requests.post(f"{Client.SERVER_URI}/contacts/search", headers=headers, json={ "pattern" : text, "offset" : 0, "count" : 50 }, verify=False)

        return response.json()["contacts"]

    def pull_messages(self, contact_id: int, message_id: int) -> dict:
        
        headers = { "Authorization" : self.__auth_token }

        response = requests.get(f"{Client.SERVER_URI}/messages/pull", headers=headers, 
                                json={ "message_id" : message_id, "user_id" : contact_id, "offset" : 0, "count" : 500 }, verify=False)

        return response.json()

    def __check_auth_token_validity(self) -> bool:

        headers = { "Authorization" : self.__auth_token }

        validate_response = requests.get(f"{Client.SERVER_URI}/account/validate", headers=headers, verify=False)

        return validate_response.status_code == 200
    
    def __connect_websocket(self) -> None:

        headers = { "Authorization" : self.__auth_token }

        self.__websocket = connect(Client.SERVER_WEBSOCKET_CONNECT_URI, ssl_context=self.__unverified_ssl_context, additional_headers=headers)

        self.__is_authorized = True
