from message_queue import message_queue as mq
from messages import NeuesSpielElement
from spielelement import SpielElement
from spieler import Spieler
from typing import List




class Arena:

    breite: int
    hoehe: int
    

    elemente: List[SpielElement]

    def __init__(self, breite: int, hoehe: int) -> None:
        self.breite = breite
        self.hoehe = hoehe
      

        self.elemente = []
        self.elemente.append(Spieler(50, 50))
        self.elemente.append(Spieler(510, 50))

    def update(self, delta_time: float):
        for objekt in self.elemente:
            objekt.update(delta_time)
        self._korrigiere_positionen()
        # self._behandle_kollisionen()
      

    def _korrigiere_positionen(self):
        for objekt in self.elemente:
            if objekt.x > 550 :
                objekt.x = 550 
                objekt.speed_x = 0
            if objekt.x < 50:
                objekt.x = 50 
                objekt.speed_x = 0
            if objekt.y > 50 :
                objekt.speed_y -= 1
            if objekt.y < 50:
                objekt.y = 50
                objekt.speed_y = 0
            if objekt.y > 550:
                objekt.y = 550
                objekt.speed_y=0
            

    # def _behandle_kollisionen(self):
    #     for a in self.elemente:
    #         for b in self.elemente:
    #             if a == b:
    #                 continue
    #             if a.hat_kollision(b):
    #                  a.on_collision(b)
        

       

    def zeichne(self):
        for objekt in self.elemente:
            objekt.zeichne()
