# standard

# vendor
import arcade
#from arcade import color


# custom
from spielelement import SpielElement
from message_queue import message_queue as mq
from messages import NeueUserEingabe, UserEingabe



class Spieler(SpielElement):
    height : float
  

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, 0, 0)  # 0, 0 für speed_x, speed_y
        self.is_jump_active = False 
        self.height = 80
        self.attack = Attack(self) # neu

       
        

    def zeichne(self):
        arcade.draw_xywh_rectangle_filled(self.x, self.y,40 ,self.height, arcade.color.AMARANTH_PINK)
        self.attack.draw()  # neu

       
      
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
                elif message.ereignis == UserEingabe.SCHLAGEN_P1:
                    self.springen()
                elif message.ereignis == UserEingabe.KEINE_EINGABE_P1:
                    self.speed_x=0
                elif message.ereignis == UserEingabe.PUNCH_P1: # neu
                    self.attack.punch()
                elif message.ereignis == UserEingabe.KICK_P1: # neu
                    self.attack.kick()    
                    
        super().update(delta_time)

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
            

class Attack:  # neu
    def __init__(self, spieler: Spieler):
        self.spieler = spieler
        self.is_punching = False
        self.is_kicking = False

    def punch(self):
        if self.is_kicking == False: #neu
            self.is_punching = True

    def kick(self):
        if self.is_punching == False: #neu
            self.is_kicking = True

    def draw(self):
        if self.is_punching:
            arcade.draw_xywh_rectangle_filled(self.spieler.x + 40, self.spieler.y + self.spieler.height / 2, 40, self.spieler.height / 2, arcade.color.RED)
            self.is_punching = False  # Reset after drawing
        if self.is_kicking:
            arcade.draw_xywh_rectangle_filled(self.spieler.x + 40, self.spieler.y, 40, self.spieler.height / 2, arcade.color.RED)
            self.is_kicking = False  # Reset after drawing
            
            


         

    

            


    