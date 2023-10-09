FROM python:3.9

WORKDIR /app

COPY client.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD python client.py

