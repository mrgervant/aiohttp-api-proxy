class RegisterRequest:
    REGISTER_URL = "*****/register"
    REGISTER_HEADERS = {
        "Content-Type": "application/json",
        "Authorization": None
    }
    REGISTER_BODY = {
        "device_name": None,
        "device_id": None
    }


class SendRequest:
    SEND_URL = "*****/send"
    SEND_HEADERS = {
        "Content-Type": "application/json",
        "Authorization": None
    }
    SEND_BODY = {
        "message": {
            "message_id": None,
            "channel_id": None,
            "payload": None
        }
    }
