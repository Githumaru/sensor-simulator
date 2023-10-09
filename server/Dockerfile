FROM python:3.9

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py /app
COPY temperature_data.json /app
COPY humidity_data.json /app
COPY waterflow_data.json /app




CMD python main.py
