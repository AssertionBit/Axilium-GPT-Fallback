FROM alpine:latest

WORKDIR /app

RUN apk add python3 gcc cmake git make

RUN python3 -m ensurepip

RUN python3 -m pip install pipenv

COPY . /app

RUN pipenv install gpt4all

EXPOSE 8000

ENTRYPOINT [ "pipenv", "run", "dev" ]

