
# vendor
from arcade import key

# custom
from messages import NeueUserEingabe
from messages import UserEingabe
from message_queue import message_queue as mq
from typing import Dict



class EingabeFilter:
    bewegungstasten_p1: Dict[int, bool]
    bewegungstasten_p2: Dict[int, bool]
    

    def __init__(self):
        self.bewegungstasten_p1 = {taste: False for taste in [ key.A, key.D,key.S, key.R,key.T ]}  # neu
        self.bewegungstasten_p2 = {taste: False for taste in [ key.J,key.K,key.L ]}



    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.W:
            mq.queue(NeueUserEingabe(UserEingabe.SPRINGEN_P1))
        if symbol == key.Y:
            mq.queue(NeueUserEingabe(UserEingabe.SCHLAGEN_P1))
        if symbol == key.I:
            mq.queue(NeueUserEingabe(UserEingabe.SPRINGEN_P2))
        if symbol == key.M:
            mq.queue(NeueUserEingabe(UserEingabe.SCHLAGEN_P2))
        if symbol in self.bewegungstasten_p1:
            self.bewegungstasten_p1[symbol] = True
        if symbol in self.bewegungstasten_p2:
            self.bewegungstasten_p2[symbol] = True
        

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in self.bewegungstasten_p1:
            self.bewegungstasten_p1[symbol] = False
            mq.queue(NeueUserEingabe(UserEingabe.KEINE_EINGABE_P1))
        if symbol in self.bewegungstasten_p2:
            self.bewegungstasten_p2[symbol] = False
            mq.queue(NeueUserEingabe(UserEingabe.KEINE_EINGABE_P2))

    def on_update(self) -> None:
        if self.bewegungstasten_p1[key.A] and not self.bewegungstasten_p1[key.D]:
            mq.queue(NeueUserEingabe(UserEingabe.LINKS_P1))
        elif self.bewegungstasten_p1[key.D] and not self.bewegungstasten_p1[key.A]:
            mq.queue(NeueUserEingabe(UserEingabe.RECHTS_P1))
        if self.bewegungstasten_p1[key.S]:
            mq.queue(NeueUserEingabe(UserEingabe.DUCKEN_P1))
        if self.bewegungstasten_p1[key.R]:
            mq.queue(NeueUserEingabe(UserEingabe.PUNCH_P1))    ## neu
        if self.bewegungstasten_p1[key.T]:
            mq.queue(NeueUserEingabe(UserEingabe.KICK_P1))      #  # neu      
       
        if self.bewegungstasten_p2[key.J] and not self.bewegungstasten_p2[key.L]:
            mq.queue(NeueUserEingabe(UserEingabe.LINKS_P2))
        elif self.bewegungstasten_p2[key.L] and not self.bewegungstasten_p2[key.J]:
            mq.queue(NeueUserEingabe(UserEingabe.RECHTS_P2))
        if self.bewegungstasten_p2[key.K]:
            mq.queue(NeueUserEingabe(UserEingabe.DUCKEN_P2))
       