import asyncio
import ssl
import websockets
import json    
import base64

uri = "wss://127.0.0.1:8080"

unverified_ssl_context = ssl._create_unverified_context()

# id = 3
headers_1 = { "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjMiLCJleHAiOjE3MjgwNDkwOTksImlzcyI6IkNvcnNhaXJNZXNzZW5nZXJTZXJ2ZXIiLCJhdWQiOiJDb3JzYWlyTWVzc2VuZ2VyQ2xpZW50In0.OqR47IoaYXffyZGgHwuIvWL78HM3ovxktfHflt7heZA" }
# id = 4
headers_2 = { "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQiLCJleHAiOjE3MjgzNzY3NDQsImlzcyI6IkNvcnNhaXJNZXNzZW5nZXJTZXJ2ZXIiLCJhdWQiOiJDb3JzYWlyTWVzc2VuZ2VyQ2xpZW50In0.FZyVN2eUXKR05NJmv0dsbfkFaIH7UUA3lxmANqhj-cE" }


async def client_1():

    async with websockets.connect(uri, ssl=unverified_ssl_context, extra_headers=headers_1) as websocket:
        while True:
            print("client_1 working")
            await websocket.send(json.dumps({ "recieverid" : 4, "text" : "hello world" }))
            await asyncio.sleep(3)

#str(base64.b64encode(b'hello world' * 1000)
async def client_2():    
    
    async with websockets.connect(uri, ssl=unverified_ssl_context, extra_headers=headers_2) as websocket:
        while True:
            print("client_2 working")
            message = await websocket.recv()
            print(json.dumps(message))

async def main():

    await asyncio.gather(client_1(), client_2())
    #await asyncio.gather(client_2())
    

if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
