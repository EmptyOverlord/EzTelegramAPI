import requests

def _request(method: str, token: str, params: dict) -> requests.Response:
    url = f"https://api.telegram.org/bot{token}/{method}"
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise ValueError(f"❗➡️ {response.text}")
    return response


def send_message(token: str, chat_id: int, text: str, *, return_message_id: bool = True) -> int | requests.Response:
    """Returns message_id if return_message_id is True, otherwise returns the Response object."""
    response = _request("sendMessage", token, {"chat_id": chat_id, "text": text})
    return response.json()["result"]["message_id"] if return_message_id else response


def edit_message(token: str, chat_id: int, message_id: int, text: str) -> requests.Response:
    """Returns the Response object."""
    return _request("editMessageText", token, {"chat_id": chat_id, "message_id": message_id, "text": text})


def delete_message(token: str, chat_id: int, message_id: int) -> requests.Response:
    """Returns the Response object."""
    return _request("deleteMessage", token, {"chat_id": chat_id, "message_id": message_id})


def forward_message(token: str, from_chat_id: int, to_chat_id: int, message_id: int) -> int:
    """Forwards a message from one chat to another. Returns message_id of the forwarded message."""
    response = _request("forwardMessage", token, {"chat_id": to_chat_id, "from_chat_id": from_chat_id, "message_id": message_id})
    return response.json()["result"]["message_id"]