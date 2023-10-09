import asyncio
import websockets
import os
from dotenv import load_dotenv

load_dotenv()


async def main():
    # Send the data to the server
    async with websockets.connect('ws://server:8765') as websocket:
        sensor_type = str(os.getenv('SENSOR_TYPE'))
        await websocket.send(sensor_type)
        frequency = str(os.getenv('DATA_FREQUENCY'))
        await websocket.send(frequency)
        # Receive the data from the server
        while True:
            data = await websocket.recv()
            print(data)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    # Handle KeyboardInterrupt to exit gracefully
    pass
except asyncio.CancelledError:
    pass
except websockets.exceptions.ConnectionClosedError:
    pass