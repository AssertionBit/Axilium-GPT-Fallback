FROM alpine:latest

WORKDIR /app

RUN apk add python3 gcc cmake git make

RUN python3 -m ensurepip

RUN python3 -m pip install pipenv

COPY . /app

# RUN chmod +x /app/scripts/deploy.sh

# RUN sh /app/scripts/deploy.sh

RUN pipenv install gpt4all

ENTRYPOINT [ "pipenv", "run", "dev" ]

