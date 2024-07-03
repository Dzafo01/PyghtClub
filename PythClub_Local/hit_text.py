from typing import Protocol
import arcade
from spieler import Spieler

class Hit_Text(Protocol):
    def hit_text(self) -> None:
        raise NotImplementedError
    

class Hit():

    def __init__(self, spieler: Spieler):
        self.spieler = spieler

    def hit_text(self):
        return arcade.draw_text('Hit',self.spieler.x,self.spieler.y,arcade.color.ALICE_BLUE)
    
class Hit_2():

    def __init__(self, spieler: Spieler):
        self.spieler = spieler

    def hit_text(self):
        return arcade.draw_text('Pow',self.spieler.x,self.spieler.y,arcade.color.ALICE_BLUE)
    
class Hit_3():

    def __init__(self, spieler: Spieler):
        self.spieler = spieler

    def hit_text(self):
        return arcade.draw_text('Boom',self.spieler.x,self.spieler.y,arcade.color.ALICE_BLUE)
    
class Hit_4():

    def __init__(self, spieler: Spieler):
        self.spieler = spieler

    def hit_text(self):
        return arcade.draw_text('Hua',self.spieler.x,self.spieler.y,arcade.color.ALICE_BLUE)