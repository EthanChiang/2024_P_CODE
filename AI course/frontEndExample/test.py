import asyncio
from websockets.server import serve
import os


async def echo(websocket):
    print('hi')
    fd = os.open("vdo", os._RDWR)
    f = os.fdopen(fd, 'wb')
    # f = open('demo.jpeg', 'wb')

    async for message in websocket:
        # print(message)
        # await websocket.send(message)
        f.write(message)
        # f.flush()
        # f.close()


async def main():
    if not os.path.exists("vdo"):
        os.mkfifo("vdo")

    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever
