# Aiohttp-based API proxy
[![CodeFactor](https://www.codefactor.io/repository/github/mrgervant/aiohttp-api-proxy/badge)](https://www.codefactor.io/repository/github/mrgervant/aiohttp-api-proxy)

Simple aiohttp-based API proxy - for simplified access to another API

## Stack
- Python 3.12
- Docker - https://docs.docker.com/get-started/overview/
- docker-compose - https://github.com/docker/compose/tree/v1
- aiohttp - https://github.com/aio-libs/aiohttp
- requests - https://github.com/psf/requests

App dependencies are installed using **poetry** - https://github.com/python-poetry/poetry

## Build with Docker
You will need Docker + docker-compose installed to build application

To create and run the image use the following command:
```
docker-compose up --build
```

The application will be available for HTTP-requests on the SERVER_PORT - specified in environments from docker-compose.yml
```
...
environment:
  MSG_USERNAME: "user@domain.com"
  MSG_PASSWORD: "password12345"
  MSG_CHANNEL: "channel12345@chat.domain.com"
  MSG_SIZE: "100"
  SERVER_NAME: "aiohttp-api-proxy"
  SERVER_PORT: "11222"
  SERVER_TOKEN: "token0123456789token"
```

## Changing the application to your API
To change the application for a specific API, adjustments are required.

Responsibility of modules:

**init.py** - main application loop (calling other modules, setting routes)

**settings.py** - parses container environment settings

**templates.py** - contains request templates for real API

**register.py** - responsible for registration on the real API

**sender.py** - responsible for sending messages in the real API

**auth_middleware.py** - security layer for checking the access token to the application

## Example request to application
```
POST http://hostname.com:11222/
Content-Type: application/json
Content-Length: 100
Authorization: *****
Body:
{
  "message": "Test message"
}
```

###### Copyright © 2024 Vladislav Popov
