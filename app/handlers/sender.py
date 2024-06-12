import logging
import json
import uuid
from http import HTTPStatus

from aiohttp import web, ClientSession

from app.config.templates import SendRequest


class Sender:
    def __init__(self, register, msg_channel, msg_size):
        self.register = register
        self.msg_channel = msg_channel
        self.msg_size = int(msg_size)

    async def send(self, request):
        request_body = await request.json()
        authorization_key = self.register.chat_api_key

        send_template = SendRequest
        url = send_template.SEND_URL
        headers = self.prepare_headers(send_template.SEND_HEADERS, authorization_key)
        body = self.prepare_body(send_template.SEND_BODY, request_body)

        async with ClientSession() as session:
            async with session.post(url, headers=headers, json=body) as send_request:
                response = await send_request.json()
                response_status = response.get("status_code", 0)
                if response_status != HTTPStatus.OK:
                    logging.error(f"Sending error: {json.dumps(response)}")
                return web.Response(text="200: Ok")

    def prepare_headers(self, headers, authorization_key):
        headers["Authorization"] = authorization_key
        return headers

    def prepare_body(self, body, request_body):
        body["message"]["message_id"] = uuid.uuid4().hex
        body["message"]["channel_id"] = self.msg_channel
        body["message"]["payload"] = self.form_payload(request_body)
        return body

    def form_payload(self, request_body):
        payload = request_body.get("message")
        payload = str(payload).strip()
        payload = payload[:self.msg_size]
        if len(payload) == 0:
            raise web.HTTPBadRequest()
        return payload
