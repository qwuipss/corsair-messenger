import asyncio
import ssl
import websockets
import json

async def main():

    uri = "wss://127.0.0.1:8080"
    context = ssl._create_unverified_context()
    
    headers1 = { "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjMiLCJleHAiOjE3MjgwNDkwOTksImlzcyI6IkNvcnNhaXJNZXNzZW5nZXJTZXJ2ZXIiLCJhdWQiOiJDb3JzYWlyTWVzc2VuZ2VyQ2xpZW50In0.OqR47IoaYXffyZGgHwuIvWL78HM3ovxktfHflt7heZA" }
    headers2 = { "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQiLCJleHAiOjE3MjgzNzY3NDQsImlzcyI6IkNvcnNhaXJNZXNzZW5nZXJTZXJ2ZXIiLCJhdWQiOiJDb3JzYWlyTWVzc2VuZ2VyQ2xpZW50In0.FZyVN2eUXKR05NJmv0dsbfkFaIH7UUA3lxmANqhj-cE" }
    import base64
    async with websockets.connect(uri, ssl=context, extra_headers=headers1) as websocket:
        while True:
            await websocket.send(json.dumps({ "recieverid" : 4, "messagetype" : "messagetype.text", "content" : str(base64.b64encode(b'hello world'), encoding='utf-8') }))
            #await asyncio.sleep(3);

    print('hello world')

if __name__ == '__main__':
    
    asyncio.run(main())