# Wind Turbine Anomaly Detection System

## Table of Contents
1. [Context](https://github.com/LuisBarbosa02/Wind-Turbine-Anomaly-Detection?tab=readme-ov-file#context)
2. [Installation](https://github.com/LuisBarbosa02/Wind-Turbine-Anomaly-Detection?tab=readme-ov-file#installation)
3. [Starting Server](https://github.com/LuisBarbosa02/Wind-Turbine-Anomaly-Detection?tab=readme-ov-file#starting-server)
4. [Model Predictions](https://github.com/LuisBarbosa02/Wind-Turbine-Anomaly-Detection?tab=readme-ov-file#model-predictions)

## Context
This project implements a real-time anomaly detection system for a wind turbine factory by using simulated sensor data.

## Installation
This repository requires Python 3.12.12 and Docker.

Clone and change to the repository:
```bash
git clone https://github.com/LuisBarbosa02/Wind-Turbine-Anomaly-Detection.git
cd Wind-Turbine-Anomaly-Detection
```

[Optional] Create and activate a virtual environment:
```bash
python3.12 -m venv venv
source venv/bin/activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

## Starting Server
The server where the model will be run and the data saved must be started. This can be done through Docker.

Within the *Wind-Turbine-Anomaly-Detection* folder, use **docker-compose.yml** to create and run the Docker containers:
```bash
docker compose up -d --build
```

## Model Predictions
With the server running, start the model predictions by running the command inside *Wind-Turbine-Anomaly-Detection*:
```bash
python sensor.py
```
