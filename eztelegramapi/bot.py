from .telegram import send_message, edit_message, delete_message, forward_message

class EzTelegramBot:
    def __init__(self, token: str):
        self.token: str = token
        self.chat_id: int = None
