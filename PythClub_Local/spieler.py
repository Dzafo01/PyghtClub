# standard
import math

# vendor
import arcade
from arcade import color


# custom
from spielelement import SpielElement
from message_queue import message_queue as mq
from messages import NeueUserEingabe, UserEingabe
#from punktliste import PunktListe


class Spieler(SpielElement):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, 0, 0)  # 0, 0 für speed_x, speed_y
        self.is_jump_active = False 
        

    def zeichne(self):
        # points = (
        #     PunktListe([(10.0, 0.0), (-5.0, -5.0), (-5.0, 5.0)])
        #     .verschiebe(self.x, self.y)
        # )
        arcade.draw_rectangle_outline(self.x, self.y,40 , 80, arcade.color.AERO_BLUE)
        

       
      
    def update(self, delta_time: float):
        for message in mq.popAll("NEUE_USER_EINGABE"):
            if isinstance(message, NeueUserEingabe):
                if message.ereignis == UserEingabe.OBEN:
                    self.beschleunige_y_pos()
                elif message.ereignis == UserEingabe.UNTEN:
                    self.beschleunige_y_neg()
                elif message.ereignis == UserEingabe.LINKS:
                    self.beschleunige_x_neg()
                elif message.ereignis == UserEingabe.RECHTS:
                    self.beschleunige_x_pos()
                elif message.ereignis == UserEingabe.Springen:
                     self.springen()
                    
        super().update(delta_time)

    def beschleunige_x_pos(self):
        self.speed_x += 0.7


    def beschleunige_x_neg(self):
        self.speed_x -= 0.7

    def springen(self):
        # self.isJumpActive = True
        self.speed_y += 15
        
            
            


         

    

            


    def __repr__(self) -> str:
        return "Spieler (%.0f/%.0f)" % (self.x, self.y)