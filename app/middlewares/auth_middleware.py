from aiohttp import web

from app.config.settings import EnvironmentVariables


@web.middleware
async def auth_middleware(request, handler):
    request_token = request.headers.get("Authorization")
    server_token = EnvironmentVariables.SERVER_TOKEN.get_env()
    if (request_token is None) or (request_token != server_token):
        raise web.HTTPUnauthorized()
    response = await handler(request)
    return response
