from abc import ABC


class BotConfig(ABC):
    def __init__(self, heart_beat_chat: int, error_notify_chat: int, bot_name: str):
        self._heart_beat_chat: int = heart_beat_chat
        self._error_notify_chat: int = error_notify_chat
        self._bot_name = bot_name

    @property
    def error_notify_chat(self) -> int:
        return self._error_notify_chat

    @property
    def heart_beat_chat(self) -> int:
        return self._heart_beat_chat

    @property
    def bot_name(self) -> str:
        return self._bot_name