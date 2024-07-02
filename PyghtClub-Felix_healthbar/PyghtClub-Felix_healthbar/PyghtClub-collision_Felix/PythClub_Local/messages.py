from enum import Enum

from message_queue import Message
from spielelement import SpielElement

class NeuesSpielElement(Message):

    elem: SpielElement

    def __init__(self, elem: SpielElement) -> None:
        super().__init__('NEUES_SPIEL_ELEMENT')
        self.elem = elem


class UserEingabe(Enum):
    SPRINGEN_P1 = 0
    LINKS_P1 = 1
    DUCKEN_P1 = 2
    RECHTS_P1 = 3
    SCHLAGEN_P1 = 4
    KEINE_EINGABE_P1 = 5
    SPRINGEN_P2 = 6
    LINKS_P2 = 7
    DUCKEN_P2 = 8
    RECHTS_P2 = 9
    SCHLAGEN_P2 = 10
    KEINE_EINGABE_P2 = 11
    PUNCH_P1 = 12 # neu
    KICK_P1 = 13 # neu
    

class NeueUserEingabe(Message):

    ereignis: UserEingabe

    def __init__(self, ereignis: UserEingabe) -> None:
        super().__init__('NEUE_USER_EINGABE')
        self.ereignis = ereignis