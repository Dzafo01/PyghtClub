from abc import ABC
from typing import Dict, List

class Message(ABC):
    """
    Eine abstrakte Basisklasse für Nachrichten im System.

    Attribute:
        type (str): Der Typ der Nachricht, der zur Unterscheidung verschiedener Nachrichtentypen verwendet wird.
    """

    type: str

    def __init__(self, type: str) -> None:
        """
        Initialisiert eine neue Instanz der Nachricht.

        Args:
            type (str): Der Typ der Nachricht.
        """
        self.type = type

class MessageQueue:
    """
    Eine Warteschlange für Nachrichten, die nach Typen organisiert ist.

    Attribute:
        messages (Dict[str, List[Message]]): Ein Wörterbuch, das Nachrichtentypen auf Listen von Nachrichten abbildet.
    """

    messages: Dict[str, List[Message]]

    def __init__(self) -> None:
        """
        Initialisiert eine neue Instanz der MessageQueue.
        Die Nachrichten werden in einem leeren Wörterbuch gespeichert.
        """
        self.messages = {}

    def queue(self, message: Message) -> None:
        """
        Fügt eine Nachricht zur Warteschlange hinzu.

        Args:
            message (Message): Die Nachricht, die zur Warteschlange hinzugefügt werden soll.
        """
        type = message.type
        if type in self.messages:
            self.messages[type].append(message)
        else:
            self.messages[type] = [message]

    def popAll(self, type: str) -> List[Message]:
        """
        Holt alle Nachrichten eines bestimmten Typs aus der Warteschlange und entfernt sie.

        Args:
            type (str): Der Typ der Nachrichten, die abgerufen werden sollen.

        Returns:
            List[Message]: Eine Liste der Nachrichten des angegebenen Typs. Wenn keine Nachrichten des Typs vorhanden sind, wird eine leere Liste zurückgegeben.
        """
        if type in self.messages:
            messages = list(self.messages[type])
            self.messages[type].clear()
            return messages
        else:
            return []
        
message_queue = MessageQueue()
