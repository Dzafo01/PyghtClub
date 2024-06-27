from enum import Enum

from message_queue import Message
from spielelement import SpielElement

class NeuesSpielElement(Message):

    elem: SpielElement

    def __init__(self, elem: SpielElement) -> None:
        super().__init__('NEUES_SPIEL_ELEMENT')
        self.elem = elem



class SpielElementVernichtet(Message):

     elem: SpielElement

     def __init__(self, elem: SpielElement) -> None:
         super().__init__('SPIEL_ELEMENT_VERNICHTET')
         self.elem = elem


class UserEingabe(Enum):
    OBEN = 0
    LINKS = 1
    UNTEN = 2
    RECHTS = 3
    Springen = 4


class NeueUserEingabe(Message):

    ereignis: UserEingabe

    def __init__(self, ereignis: UserEingabe) -> None:
        super().__init__('NEUE_USER_EINGABE')
        self.ereignis = ereignis