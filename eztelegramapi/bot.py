from .telegram import send_message, edit_message, delete_message, forward_message

class EzTelegramBot:
    def __init__(self, token: str, chat_id: int | None = None):
        self.token: str = token
        self.chat_id: int | None = chat_id

    def _resolve_chat_id(self, chat_id: int | None) -> int:
        resolved = chat_id or self.chat_id
        if resolved is None:
            raise ValueError("❗➡️ chat_id is not set — pass it explicitly or set self.chat_id")
        return resolved

    def send_message(self, text: str, chat_id: int | None = None) -> int:
        return send_message(
            token=self.token,
            chat_id=self._resolve_chat_id(chat_id), # type:ignore
            text=text
        )

    def edit_message(self, message_id: int, text: str, chat_id: int | None = None):
        return edit_message(
            token=self.token,
            chat_id=self._resolve_chat_id(chat_id),
            message_id=message_id,
            text=text
        )

    def delete_message(self, message_id: int, chat_id: int | None = None):
        return delete_message(
            token=self.token,
            chat_id=self._resolve_chat_id(chat_id),
            message_id=message_id
        )

    def forward_message(self, from_chat_id: int, message_id: int, to_chat_id: int | None = None):
        return forward_message(
            token=self.token,
            from_chat_id=from_chat_id,
            to_chat_id=self._resolve_chat_id(to_chat_id),
            message_id=message_id
        )