import json
import asyncio
import websockets
import requests
from datetime import datetime, timedelta
import random


api_key = "DmYzWP5ba4RMdCBgKgRYoOy6W20GGsPK"

class TemperatureSensor():
    def __init__(self):
        self.temperature = None
        self.current_index = 0

        # Load sensor data from the 'temperature_data.json' file
        with open('temperature_data.json', 'r') as file:
            weather_data = json.load(file)
        self.sensor_data = weather_data['data']['timelines'][0]['intervals']

    def create_file(self):
        # Function to create a file with weather data

        # Set the latitude and longitude for the weather location
        latitude = '52.5200'
        longitude = '13.4050'

        # Get the current time and set the start and end times for fetching weather data
        current_time = datetime.now().replace(minute=0, second=0, microsecond=0)
        start_time = current_time - timedelta(hours=23)
        start_time_str = start_time.isoformat() + "Z"
        end_time_str = current_time.isoformat() + "Z"

        # Specify the fields to fetch from the weather API
        fields = 'temperature'

        # Create the API URL with the specified parameters
        url = f'https://api.tomorrow.io/v4/timelines?location={latitude},{longitude}&fields={fields}&startTime={start_time_str}&endTime={end_time_str}&apikey={api_key}'

        # Send a GET request to the API and fetch the weather data
        response = requests.get(url)
        weather_data = response.json()

        # Manipulate the fetched weather data
        timeline = weather_data['data']['timelines'][0]['intervals'].copy()
        k = 0
        for point in timeline:
            time = point['startTime']
            temp = point['values']['temperature']
            new_time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
            for i in range(149):
                new_temp = round(random.uniform(temp - 1, temp + 1), 2)
                new_time += timedelta(seconds=24)
                weather_data['data']['timelines'][0]['intervals'].insert(k * 150 + i + 1,
                                                                         {"startTime": new_time.isoformat() + "Z",
                                                                          "values": {"temperature": new_temp}})
            k += 1

        # Save the manipulated weather data to a file named 'weather_data.json'
        with open('temperature_data.json', 'w') as file:
            json.dump(weather_data, file)

    def read_sensor_data(self):
        # Function to read sensor data
        if self.current_index >= len(self.sensor_data):
            self.current_index = 0
        self.temperature = self.sensor_data[self.current_index]['values']['temperature']
        self.current_index += 1

    async def send_data(self, websocket):
        # Function to send data to the server
        await websocket.send(str(self.temperature))


class HumiditySensor():
    def __init__(self):
        self.humidity = None
        self.current_index = 0

        # Load sensor data from the 'humidity_data.json' file
        with open('humidity_data.json', 'r') as file:
            self.sensor_data = json.load(file)


    def create_file(self):
        # Function to create a file with humidity data
        list_of_data = []
        start_data = random.randint(200, 1000)
        list_of_data.append(start_data)
        data = start_data
        for _ in range(3599):
            data = random.randint(data - 10, data + 10)
            while data < 200 or data > 1000:
                data = random.randint(start_data - 10, start_data + 10)
            start_data = data
            list_of_data.append(start_data)

        with open('humidity_data.json', 'w') as file:
            json.dump(list_of_data, file)

    def read_sensor_data(self):
        # Function to read sensor data
        if self.current_index >= len(self.sensor_data):
            self.current_index = 0
        self.humidity = self.sensor_data[self.current_index]
        self.current_index += 1

    async def send_data(self, websocket):
        # Function to send data to the server
        await websocket.send(str(self.humidity))

class WaterFlowSensor():
    def __init__(self):
        self.waterflow = None
        self.current_index = 0

        # Load sensor data from the 'humidity_data.json' file
        with open('waterflow_data.json', 'r') as file:
            self.sensor_data = json.load(file)

    def create_file(self):
        # Function to create a file with humidity data
        list_of_data = []
        for _ in range(2):
            for _ in range(600):
                list_of_data.append(random.randint(1, 100))
            for _ in range(300):
                list_of_data.append(random.randint(100, 500))
            for _ in range(600):
                list_of_data.append(random.randint(500, 10000))
            for _ in range(300):
                list_of_data.append(random.randint(100, 500))

        with open('waterflow_data.json', 'w') as file:
            json.dump(list_of_data, file)

    def read_sensor_data(self):
        # Function to read sensor data
        if self.current_index >= len(self.sensor_data):
            self.current_index = 0
        self.waterflow = self.sensor_data[self.current_index]
        self.current_index += 1

    async def send_data(self, websocket):
        # Function to send data to the client
        await websocket.send(str(self.waterflow))


async def run(websocket):
    # Receive the data from the client
    sensor_type = await websocket.recv()
    sensor = create_sensor(sensor_type)
    frequency = int(await websocket.recv())
    # Send the data to the client
    while True:
        try:
            sensor.read_sensor_data()
            await sensor.send_data(websocket)
            await asyncio.sleep(frequency)
        except asyncio.exceptions.IncompleteReadError:
            pass
        except websockets.exceptions.ConnectionClosedError:
            pass


def create_sensor(sensor_type):
    # Create a sensor based on the given sensor type
    if sensor_type == 'temperature':
        return TemperatureSensor()
    elif sensor_type == 'humidity':
        return HumiditySensor()
    elif sensor_type == 'waterflow':
        return WaterFlowSensor()

async def main():
    async with websockets.serve(run, "0.0.0.0", 8765):
        await asyncio.Future()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    # Handle KeyboardInterrupt to exit gracefully
    pass





