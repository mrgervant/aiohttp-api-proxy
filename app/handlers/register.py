import logging
import json
import base64
from http import HTTPStatus

from requests import post

from app.config.templates import RegisterRequest


class Register:
    def __init__(self, username, password, hostname, hostport):
        self.register_auth = self.basic_auth(username, password)
        self.hostname = hostname
        self.hostport = hostport

        register_template = RegisterRequest
        self.url = register_template.REGISTER_URL
        self.headers = self.prepare_headers(register_template.REGISTER_HEADERS)
        self.body = self.prepare_body(register_template.REGISTER_BODY)

        self._chat_api_key = None
        self.register_chat_api()

    def register_chat_api(self):
        register_request = post(self.url, headers=self.headers, json=self.body)
        response = register_request.json()
        response_status = response.get("status_code", 0)
        if response_status != HTTPStatus.OK:
            logging.error(f"Registration error: {json.dumps(response)}")
            raise SystemExit
        chat_username = response["chat_username"]
        chat_password = response["chat_password"]
        self._chat_api_key = self.basic_auth(chat_username, chat_password)

    def prepare_headers(self, headers):
        headers["Authorization"] = self.register_auth
        return headers

    def prepare_body(self, body):
        body["device_name"] = self.hostname
        body["device_id"] = f"{self.hostname}{self.hostport}"
        return body

    @staticmethod
    def basic_auth(username, password):
        token = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
        return f"Basic {token}"

    @property
    def chat_api_key(self):
        return self._chat_api_key
