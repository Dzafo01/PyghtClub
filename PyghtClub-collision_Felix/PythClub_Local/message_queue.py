
from abc import ABC
from typing import Dict, List


class Message(ABC):

    type: str

    def __init__(self, type: str) -> None:
        self.type = type


class MessageQueue:

    messages: Dict[str, List[Message]]

    def __init__(self) -> None:
        self.messages = {}

    def queue(self, message: Message):
        type = message.type
        if type in self.messages:
            self.messages[type].append(message)
        else:
            self.messages[type] = [message]

    def popAll(self, type: str) -> List[Message]:
        if type in self.messages:
            messages = list(self.messages[type])
            self.messages[type].clear()
            return messages
        else:
            return []
        
message_queue = MessageQueue()