# <span style="font-size:20px;">Sensor-simulator</span>
The app simulates behavior of a sensor
Sensor simulator

# <span style="font-size:20px;">Overview</span>
The Sensor Project is a Python-based application that simulates sensor's behavior and communicates it between a server and client using WebSocket technology. 
This project provides a framework for creating different types of sensor modules, such as temperature, humidity, and water flow sensors. These modules read simulated sensor data and send it to a central 
server, which then forwards the data to connected clients over WebSocket connections.

# <span style="font-size:20px;">Table of Contents</span>
Features
Installation
Usage
Configuration
Contributing
License

# <span style="font-size:20px;">Features</span>
Simulates different types of sensor data.
WebSocket-based communication between sensors, server, and clients.
Easily extensible to add new sensor types.
Supports concurrent connections and data streaming.

# <span style="font-size:20px;">Installation</span>

To run this project, you'll need Docker installed on your system.

## <span style="font-size:12px;">Clone the Repository:</span>

Clone this repository to your local machine using [Git](https://git-scm.com/):

```
git clone https://github.com/Githumaru/sensor-simulator.git
cd sensor-simulator
```

## <span style="font-size:12px;">Build the Docker Containers:</span>

In the project root directory, you'll find a docker-compose.yml file. This file defines the services and configurations for both the server and client containers.

## <span style="font-size:12px;">To build the Docker containers, open your terminal and run:</span>

```
docker-compose build
```

This command will build the Docker images defined in the Dockerfile for the server and client.

## <span style="font-size:12px;">Create Dummy Data Files:</span>

The server container relies on data files like temperature_data.json, humidity_data.json, and waterflow_data.json. You can manually create these files in the server/ directory or generate them programmatically. If you have scripts to generate these files, run them now.

## <span style="font-size:20px;">Start the Docker Containers:</span>

Once the containers are built and the data files are ready, you can start the services:

```
docker-compose up
```

# <span style="font-size:20px;">Sensor Modules</span>
You can create custom sensor modules by inheriting from the Sensor class and implementing the necessary methods.

Add your sensor module to the server by importing it and creating an instance in the server.py script.

# <span style="font-size:20px;">Configuration</span>
The server and client WebSocket endpoints can be configured in the respective scripts.
