import requests

def send_message(TOKEN: str, CHAT_ID: int, text: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r_object = requests.get(url, params={
        "chat_id": CHAT_ID,
        "text": text
    })

    if r_object.status_code == 200:
        return r_object
    else:
        raise ValueError(r_object.text)
