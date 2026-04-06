import requests

def send_message(TOKEN: str, CHAT_ID: int, text: str ,*,return_message_id=True) -> int | requests.Response:
    '''returns the message_id of the sent message if return_message_id is True, otherwise returns the response object.'''

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r_object = requests.get(url, params={
        "chat_id": CHAT_ID,
        "text": text
    })

    if r_object.status_code == 200:
        if return_message_id:
            return r_object.json()["result"]["message_id"]
        else:
            return r_object
    else:
        raise ValueError(f"❗➡️ {r_object.text}")

def edit_message(TOKEN: str, CHAT_ID: int, MESSAGE_ID: int, text: str) -> requests.Response:
    '''returns the response object.'''

    url = f"https://api.telegram.org/bot{TOKEN}/editMessageText"
    r_object = requests.get(url, params={
        "chat_id": CHAT_ID,
        "message_id": MESSAGE_ID,
        "text": text
    })
    if r_object.status_code == 200:
        return r_object
    else:
        raise ValueError(f"❗➡️ {r_object.text}")
