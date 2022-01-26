FROM python:3.9-slim

WORKDIR /app

ADD . /app

RUN python -m pip install -r requirements.txt

CMD python main.py