FROM python:3.9-slim

WORKDIR /app

ADD . /app

EXPOSE 8000

RUN python -m pip install -r requirements.txt

CMD python main.py
