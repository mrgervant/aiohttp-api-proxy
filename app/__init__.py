import logging

from aiohttp import web

from app.handlers.register import Register
from app.handlers.sender import Sender
from app.middlewares.auth_middleware import auth_middleware
from app.config.settings import EnvironmentVariables


def main():
    logging.basicConfig(
        format="%(asctime)s.%(msecs)03d - [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO
    )

    register = Register(
        username=EnvironmentVariables.MSG_USERNAME.get_env(),
        password=EnvironmentVariables.MSG_PASSWORD.get_env(),
        hostname=EnvironmentVariables.SERVER_NAME.get_env(),
        hostport=EnvironmentVariables.SERVER_PORT.get_env()
    )

    sender = Sender(
        register,
        msg_channel=EnvironmentVariables.MSG_CHANNEL.get_env(),
        msg_size=EnvironmentVariables.MSG_SIZE.get_env(),
    )

    app = web.Application(middlewares=[auth_middleware])
    app.add_routes([web.post("/", sender.send)])

    logging.info("Application launched")
    web.run_app(
        app,
        port=int(EnvironmentVariables.SERVER_PORT.get_env()),
        access_log_format='"%r" - %s (%Tf) - %a'
    )
    logging.info("Application stopped")
