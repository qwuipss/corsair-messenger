import json
import requests
from SharedConstants import SECOND_WINDOW
from json import JSONEncoder
from collections.abc import Iterable
from websockets.sync.client import connect
from os.path import dirname, realpath, exists

class Client:

    __SERVER_IP_ADDRESS_PORT = "localhost:8080"

    __SERVER_URI = f"https://{__SERVER_IP_ADDRESS_PORT}"

    __SERVER_WEBSOCKET_CONNECT_URI = f"wss://{__SERVER_IP_ADDRESS_PORT}"

    __AUTH_TOKEN_LOAD_FILENAME = f"{dirname(realpath(__file__))}/auth.json"

    CONTACTS_FIRST_LOAD_COUNT = 15

    __CONTACTS_SEARCH_LOAD_COUNT = 15

    CONTACTS_AFTER_LOAD_COUNT = 5

    MESSAGES_LOAD_COUNT = 10

    __LOCAL_STARTUP = True

    if SECOND_WINDOW:
        __SECOND_WINDOW_AUTH_TOKEN_LOAD_FILENAME = f"{dirname(realpath(__file__))}/authSecondWindow.json"
        __first_auth = True

    def __init__(self) -> None:
        
        if Client.__LOCAL_STARTUP:
            
            from ssl import _create_unverified_context
            from urllib3 import disable_warnings 
            from urllib3.exceptions import InsecureRequestWarning 
    
            disable_warnings(InsecureRequestWarning)

            self.__ssl_context = _create_unverified_context()
            
        else:

            self.__ssl_context = None

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

            if not exists(Client.__SECOND_WINDOW_AUTH_TOKEN_LOAD_FILENAME):
                return (False, "")
            
            with open(Client.__SECOND_WINDOW_AUTH_TOKEN_LOAD_FILENAME, "r") as file:
                try:
                    loaded_file = json.load(file)
                except:
                    pass

        else:

            if not exists(Client.__AUTH_TOKEN_LOAD_FILENAME):
                return (False, "")

            with open(Client.__AUTH_TOKEN_LOAD_FILENAME, "r") as file:
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
            with open(Client.__SECOND_WINDOW_AUTH_TOKEN_LOAD_FILENAME, "w") as file:
                file.write(json.dumps(data))
        else:
            with open(Client.__AUTH_TOKEN_LOAD_FILENAME, "w") as file:
                file.write(json.dumps(data))

    def auth(self, login: str, password: str) -> bool:
        
        if not isinstance(login, str):
            raise ValueError(login)
        
        if not isinstance(password, str):
            raise ValueError(password)

        auth_response = requests.post(f"{Client.__SERVER_URI}/account/login", json={ "login" : login, "password" : password }, verify=not Client.__LOCAL_STARTUP)

        if auth_response.status_code == 200:

            self.__is_authorized = True
            
            self.__auth_token = "Bearer " + auth_response.json()["token"]

            self.__connect_websocket()
            self.__save_auth_token(self.__auth_token)

            Client.__first_auth = False

            return True
        
        return False

    def receive_message(self) -> None:

        if not self.__is_authorized:
            raise ValueError(self.__is_authorized)

        message = self.__websocket.recv()
        
        return message

    def send_message(self, **message) -> None:

        if not self.__is_authorized:
            raise ValueError(self.__is_authorized)
        
        serialized_message = JSONEncoder().encode(message)

        self.__websocket.send(serialized_message)

    def get_contacts(self, offset: int, count: int) -> tuple[bool, Iterable[dict]]:
        
        if not self.__is_authorized:
            raise ValueError(self.__is_authorized)
        
        if not isinstance(offset, int):
            raise TypeError(type(offset))

        headers = { "Authorization" : self.__auth_token }

        json = { "offset" : offset, "count" : count }

        response = requests.get(f"{Client.__SERVER_URI}/contacts/get-many", headers=headers, json=json, verify=not Client.__LOCAL_STARTUP)

        contacts = response.json()["contacts"]

        return (len(contacts) == count, contacts)

    def get_contact(self, id: int) -> dict:

        if not self.__is_authorized:
            raise ValueError(self.__is_authorized)
        
        if not isinstance(id, int):
            raise TypeError(type(id))

        headers = { "Authorization" : self.__auth_token }

        json = { "id" : id }

        response = requests.get(f"{Client.__SERVER_URI}/contacts/get-single", headers=headers, json=json, verify=not Client.__LOCAL_STARTUP)

        contact = response.json()["contact"]

        return contact

    def search_contacts(self, pattern: str) -> Iterable[dict]:

        if not isinstance(pattern, str):
            raise TypeError(type(pattern))

        json = { "pattern" : pattern, "count" : Client.__CONTACTS_SEARCH_LOAD_COUNT }

        response = requests.post(f"{Client.__SERVER_URI}/contacts/search", json=json, verify=not Client.__LOCAL_STARTUP)

        return response.json()["contacts"]

    def load_messages(self, user_id: int, message_id: int) -> tuple[bool, Iterable[dict]]:
        
        if not isinstance(user_id, int):
            raise TypeError(type(user_id))
        
        if not isinstance(message_id, int):
            raise TypeError(type(message_id))

        if not self.__is_authorized:
            raise ValueError(self.__is_authorized)

        headers = { "Authorization" : self.__auth_token }

        json = { "message_id" : message_id, "user_id" : user_id, "count" : Client.MESSAGES_LOAD_COUNT }

        response = requests.get(f"{Client.__SERVER_URI}/messages/load", headers=headers, json=json, verify=not Client.__LOCAL_STARTUP)

        messages = response.json()["messages"]

        return (len(messages) == Client.MESSAGES_LOAD_COUNT, messages)

    def __check_auth_token_validity(self) -> bool:

        headers = { "Authorization" : self.__auth_token }

        validate_response = requests.get(f"{Client.__SERVER_URI}/account/validate", headers=headers, verify=not Client.__LOCAL_STARTUP)

        return validate_response.status_code == 200
    
    def __connect_websocket(self) -> None:

        if not self.__is_authorized:
            raise ValueError(self.__is_authorized)

        headers = { "Authorization" : self.__auth_token }

        self.__websocket = connect(Client.__SERVER_WEBSOCKET_CONNECT_URI, ssl_context=self.__ssl_context, additional_headers=headers)

        self.__is_authorized = True
