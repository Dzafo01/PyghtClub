# standard

# vendor
import arcade
#from arcade import color


# custom
from spielelement import SpielElement
from message_queue import message_queue as mq
from messages import NeueUserEingabe, UserEingabe
from interfaces import Temporaer,Permanent


class Spieler(SpielElement):
    health:float
    speed_x: float
    speed_y : float
    

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y,80,40) 
        self.attack = Attack(self) # neu
        self.health = 100
        self.speed_x =  0
        self.speed_y = 0
    
        

    def zeichne(self):
        arcade.draw_xywh_rectangle_filled(self.x, self.y,self.width ,self.height, arcade.color.AMARANTH_PINK)
        self.attack.zeichne()  # neu

       
      
    def update(self, delta_time: float):
        for message in mq.popAll("NEUE_USER_EINGABE"):
            if isinstance(message, NeueUserEingabe):
                if message.ereignis == UserEingabe.SPRINGEN_P1:
                    self.springen()
                elif message.ereignis == UserEingabe.DUCKEN_P1:
                    self.ducken()
                else:
                    self.height=80
                if message.ereignis == UserEingabe.LINKS_P1:
                    self.beschleunige_x_neg()
                elif message.ereignis == UserEingabe.RECHTS_P1:
                    self.beschleunige_x_pos()
                elif message.ereignis == UserEingabe.KEINE_EINGABE_P1:
                    self.speed_x=0
                elif message.ereignis == UserEingabe.PUNCH_P1: # neu
                    self.attack.punch()
                elif message.ereignis == UserEingabe.KICK_P1: # neu
                    self.attack.kick()             
        self.y += self.speed_y
        self.x += self.speed_x

    def beschleunige_x_pos(self):
        self.x += 5

    def beschleunige_x_neg(self):
        self.x -= 5

    def springen(self):
        self.speed_y += 15

    def ducken(self):
        self.height= 40
    
    def __repr__(self) -> str:
        return "Spieler (%.0f/%.0f)" % (self.x, self.y)

    def on_collision(self, elem: 'SpielElement'):
        if isinstance(elem,Permanent):
            self.x= elem.x - elem.width 
              

class Attack(SpielElement):  # neu
    
    def __init__(self, spieler: Spieler):
        self.spieler = spieler
        self.is_punching = False
        self.is_kicking = False
        self.x = spieler.x
        self.y = spieler.y
        self.height = spieler.height
        self.width = spieler.width
      

    def punch(self):
        if self.is_kicking == False: #neu
            self.is_punching = True

    def kick(self):
        if self.is_punching == False: #neu
            self.is_kicking = True
    
    def on_collision(self, elem: 'Spieler'):
        if elem != self.spieler:
            elem.health -= 10
            print(elem.health)

    def zeichne(self):
        self.x = self.spieler.x + 40
        if self.is_punching:
            arcade.draw_xywh_rectangle_filled(self.x, self.spieler.y + self.spieler.height / 2, self.spieler.width , self.spieler.height / 2, arcade.color.RED)
            self.is_punching = False  # Reset after drawing
        if self.is_kicking:
            arcade.draw_xywh_rectangle_filled(self.x, self.spieler.y, self.spieler.width, self.spieler.height / 2, arcade.color.RED)
            self.is_kicking = False  # Reset after drawing
    



# draw healthbar in spieler -> zeichne()
# delay für andere aktionen nach schlag/tritt
# 2. spieler inputs und schlag/tritt drehen
# runde gewonnen -> zurücksetzen der arena und zähler aus 1 : 0
# Spiel gewonnen -> 2 von 3 runden gewonnen -> Spiel gewonnen schriftzug und spiel zurücksetzen
# draw verschiedene textnachrichten über spieler wenn spieler gehittet (Protokoll)   


         

    

            


    