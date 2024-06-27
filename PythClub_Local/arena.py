from message_queue import message_queue as mq
from messages import SpielElementVernichtet, NeuesSpielElement
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
        

    def update(self, delta_time: float):
        for objekt in self.elemente:
            objekt.update(delta_time)
        self._korrigiere_positionen()
        self._behandle_kollisionen()
        self._bearbeite_nachrichten()

    def _korrigiere_positionen(self):
        for objekt in self.elemente:
            if objekt.x > 550 :
                objekt.x = 550 
                objekt.speed_x = 0
            if objekt.x < 50:
                objekt.x = 50 
                objekt.speed_x = 0
            if objekt.y > 50 :
                objekt.speed_y -= 2
            if objekt.y < 50:
                objekt.y = 50
                objekt.speed_y = 0
            

    def _behandle_kollisionen(self):
        for a in self.elemente:
            for b in self.elemente:
                if a == b:
                    continue
                if a.hat_kollision(b):
                     a.on_collision(b)
        
    def _bearbeite_nachrichten(self):
        for nachricht in mq.popAll('SPIEL_ELEMENT_VERNICHTET'):
            if isinstance(nachricht, SpielElementVernichtet):
                if nachricht.elem in self.elemente:
                    self.elemente.remove(nachricht.elem)

       

    def zeichne(self):
        for objekt in self.elemente:
            objekt.zeichne()
