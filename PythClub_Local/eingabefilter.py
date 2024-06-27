
# vendor
from arcade import key

# custom
from messages import NeueUserEingabe
from messages import UserEingabe
from message_queue import message_queue as mq
from typing import Dict

class EingabeFilter:
    bewegungstasten: Dict[int, bool]

    def __init__(self):
        self.bewegungstasten = {taste: False for taste in [key.W, key.A, key.S, key.D]}

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.SPACE:
            mq.queue(NeueUserEingabe(UserEingabe.Springen))
        if symbol in self.bewegungstasten:
            self.bewegungstasten[symbol] = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in self.bewegungstasten:
            self.bewegungstasten[symbol] = False

    def on_update(self) -> None:
        if self.bewegungstasten[key.W] and not self.bewegungstasten[key.S]:
            mq.queue(NeueUserEingabe(UserEingabe.OBEN))
        elif self.bewegungstasten[key.S] and not self.bewegungstasten[key.W]:
            mq.queue(NeueUserEingabe(UserEingabe.UNTEN))
        if self.bewegungstasten[key.A] and not self.bewegungstasten[key.D]:
            mq.queue(NeueUserEingabe(UserEingabe.LINKS))
        elif self.bewegungstasten[key.D] and not self.bewegungstasten[key.A]:
            mq.queue(NeueUserEingabe(UserEingabe.RECHTS))