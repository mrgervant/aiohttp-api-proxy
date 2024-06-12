from os import environ
from enum import Enum


class EnvironmentVariables(str, Enum):
    MSG_USERNAME = "MSG_USERNAME"
    MSG_PASSWORD = "MSG_PASSWORD"
    MSG_CHANNEL = "MSG_CHANNEL"
    MSG_SIZE = "MSG_SIZE"
    SERVER_NAME = "SERVER_NAME"
    SERVER_PORT = "SERVER_PORT"
    SERVER_TOKEN = "SERVER_TOKEN"

    def get_env(self, variable=None):
        return environ.get(self, variable)
