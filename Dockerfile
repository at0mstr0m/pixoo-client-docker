# syntax=docker/dockerfile:1

FROM python:3.8.13

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV PORT=1337

CMD [ "python3", "app.py"]

EXPOSE 1337