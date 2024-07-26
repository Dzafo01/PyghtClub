from enum import Enum

from message_queue import Message
from spielelement import SpielElement

class NeuesSpielElement(Message):

    elem: SpielElement

    def __init__(self, elem: SpielElement) -> None:
        super().__init__('NEUES_SPIEL_ELEMENT')
        self.elem = elem

class NeueHitMessage(Message):

    elem: SpielElement

    def __init__(self, elem: SpielElement) -> None:
        super().__init__('NEUE_HIT_MESSAGE')
        self.elem = elem


class UserEingabe(Enum):
    SPRINGEN_P1 = 0
    DUCKEN_P1 = 1
    LINKS_P1 = 2
    RECHTS_P1 = 3
    KEINE_EINGABE_P1 = 4
    SPRINGEN_P2 = 5
    DUCKEN_P2 = 6
    LINKS_P2 = 7
    RECHTS_P2 = 8
    KEINE_EINGABE_P2 = 9
    PUNCH_P1 = 10 # neu
    KICK_P1 = 11# neu
    PUNCH_P2 = 12
    KICK_P2 = 13
    

class NeueUserEingabe_P1(Message):

    ereignis: UserEingabe

    def __init__(self, ereignis: UserEingabe) -> None:
        super().__init__('NEUE_USER_EINGABE_P1')
        self.ereignis = ereignis

class NeueUserEingabe_P2(Message):

    ereignis: UserEingabe

    def __init__(self, ereignis: UserEingabe) -> None:
        super().__init__('NEUE_USER_EINGABE_P2')
        self.ereignis = ereignis