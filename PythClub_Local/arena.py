from message_queue import message_queue as mq
from messages import NeuesSpielElement
from spielelement import SpielElement
from spieler import Spieler
from typing import List
from spieler import Attack
from interfaces import Permanent,Temporaer




class Arena:

    breite: int
    hoehe: int
    elemente: List[SpielElement]

    def __init__(self, breite: int, hoehe: int) -> None:
        self.breite = breite
        self.hoehe = hoehe
        self._init_elemente()  

    def _init_elemente(self): 
        self.elemente = []
        self.elemente.append(Spieler(50, 50,1))
        self.elemente.append(Spieler(510, 50,2))
    
    
    def update(self, delta_time: float):
        for objekt in self.elemente: 
            objekt.update(delta_time)
        self._korrigiere_positionen()
        self._check_health()  
        self.hitbox(self.elemente[0])
        self.hitbox(self.elemente[1])
        self._behandle_kollisionen()
          
    def _check_health(self):  
        for objekt in self.elemente:
            if isinstance(objekt, Spieler) and objekt.health <= 0:
                self.reset_arena()

    def reset_arena(self):  
        self._init_elemente()         
            
       
    def hitbox(self, elem : SpielElement):
        if elem.attack.is_kicking or elem.attack.is_punching:
            self.elemente.append(elem.attack)      

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
            

    def _behandle_kollisionen(self):
        for a in self.elemente:
            for b in self.elemente:
                if a == b:
                    continue
                if isinstance(a, Permanent) & isinstance(b, Permanent):
                    if(a.x < b.x):
                        a.attack.is_left = True
                    else:
                        a.attack.is_left = False
                if a.hat_kollision(b):
                    a.on_collision(b)
            if isinstance(a,Temporaer):
                self.elemente.pop(-1)
           
        

    def zeichne(self):
        for objekt in self.elemente:
            objekt.zeichne()
