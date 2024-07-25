# standard
from typing import Protocol
import random

# vendor
import arcade
#from arcade import color


# custom
from spielelement import SpielElement
from message_queue import message_queue as mq
from messages import NeueUserEingabe_P1,NeueUserEingabe_P2, UserEingabe
from interfaces import Temporaer,Permanent



class Spieler(SpielElement):
    health:float
    speed_x: float
    speed_y : float
    cooldown : float
    on_cooldown : bool
    timer:float
    player : int       
   

    def __init__(self, x: float, y: float, player:int) -> None:
        super().__init__(x, y,80,40) 
        self.attack = Attack(self) # neu
        self.health = 100
        self.speed_x =  0
        self.speed_y = 0
        self.cooldown = 0
        self.on_cooldown = True
        self.timer = 30 
        self.player = player
       
    
    def setup(self):
        self.health = 100
        self.speed_x = 0
        self.speed_y = 0
        self.cooldown = 0
        self.on_cooldown = True
        self.player_dead = False
        self.timer = 30     
    
    def zeichne_healthbar_P1(self):     
        ratio = self.health / 100
        if self.health < 0:
           ratio = 0
        arcade.draw_xywh_rectangle_filled(49,499,202,32,arcade.color.WHITE)
        arcade.draw_xywh_rectangle_filled(50,500,200*ratio,30,arcade.color.RED) #  pfusch lösung
       
        
    def zeichne_healthbar_P2(self):       
        ratio = self.health / 100
        if self.health < 0:
            ratio= 0
        arcade.draw_xywh_rectangle_filled(349,499,202,32,arcade.color.WHITE)
        arcade.draw_xywh_rectangle_filled(350,500,200*ratio,30,arcade.color.RED)      
    
    def zeichne_timer(self):
        seconds = int(self.timer) % 60
        timer_text = f"{seconds:02d}"
        arcade.draw_text(timer_text, 300, 510, arcade.color.WHITE, 20, anchor_x="center")

        

    def zeichne(self):
        arcade.draw_xywh_rectangle_filled(self.x, self.y,self.width ,self.height, arcade.color.AMARANTH_PINK)
        self.attack.zeichne()
        if self.player == 1:  
            self.zeichne_healthbar_P1()
        elif self.player == 2:
            self.zeichne_healthbar_P2()
        self.zeichne_timer()  
        

    def update(self, delta_time: float):
        if self.player == 1:
            for message in mq.popAll("NEUE_USER_EINGABE_P1"):
                if isinstance(message, NeueUserEingabe_P1):   
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
                        self.on_cooldown = False
                    elif message.ereignis == UserEingabe.KICK_P1: # neu
                        self.attack.kick()
                        self.on_cooldown = False 
        if self.player == 2:
            for message in mq.popAll("NEUE_USER_EINGABE_P2"):
                if isinstance(message, NeueUserEingabe_P2):    
                    if message.ereignis == UserEingabe.SPRINGEN_P2:
                        print('springen')
                        self.springen()
                    elif message.ereignis == UserEingabe.DUCKEN_P2:
                        self.ducken()
                    else:
                        self.height=80
                    if message.ereignis == UserEingabe.LINKS_P2:
                        self.beschleunige_x_neg()
                    elif message.ereignis == UserEingabe.RECHTS_P2:
                        self.beschleunige_x_pos()
                    elif message.ereignis == UserEingabe.KEINE_EINGABE_P2:
                        self.speed_x=0
                    elif message.ereignis == UserEingabe.PUNCH_P2: # neu
                        self.attack.punch()
                        self.on_cooldown = False
                    elif message.ereignis == UserEingabe.KICK_P2: # neu
                        self.attack.kick()
                        self.on_cooldown = False
        self.y += self.speed_y
        self.x += self.speed_x
        if(self.on_cooldown == False):
            self.cooldown += 1
        if (self.cooldown > 40):
            self.cooldown = 0
            self.on_cooldown = True
        
        self.timer -= delta_time
        if self.timer <= 0:
            self.timer = 0
            self.reset_fighter()


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

    def reset_fighter(self):
        self.setup()
        self.zeichne()
   

              

class Attack(SpielElement):  # neu
    is_left : bool
    text : 'Hit_Text'
    
    def __init__(self, spieler: Spieler):
        self.spieler = spieler
        self.is_punching = False
        self.is_kicking = False
        self.x = spieler.x
        self.y = spieler.y
        self.height = spieler.height
        self.width = spieler.width
        self.is_left = False
        self.text = Hit_Text
      

    def punch(self):
        if self.spieler.on_cooldown == True: #neu
            self.is_punching = True

    def kick(self):
        if self.spieler.on_cooldown == True: #neu
            self.is_kicking = True

    def shuffle_text(self):
        rand = random.choice([Hit.hit_text(self),Hit_2.hit_text(self),Hit_3.hit_text(self),Hit_4.hit_text(self)])
        return rand
    
    def on_collision(self, elem: 'Spieler'):
        if elem != self.spieler:
            elem.health -= 10
            # self.text = self.shuffle_text()
           
             

    def zeichne(self):
        if (self.is_left):
            self.x = self.spieler.x + self.spieler.width
        else:
            self.x = self.spieler.x - self.spieler.width
        if self.is_punching:
            arcade.draw_xywh_rectangle_filled(self.x, self.spieler.y + self.spieler.height / 2, self.spieler.width , self.spieler.height / 2, arcade.color.RED)
            self.is_punching = False  # Reset after drawing
        if self.is_kicking:
            arcade.draw_xywh_rectangle_filled(self.x, self.spieler.y, self.spieler.width, self.spieler.height / 2, arcade.color.RED)
            self.is_kicking = False  # Reset after drawing
        # if self.hat_kollision():
        #     self.text.draw()
            
    


class Hit_Text(Protocol):
    def hit_text(self) -> None:
        raise NotImplementedError
    

class Hit():

    def __init__(self, spieler: Spieler):
        self.spieler = spieler

    def hit_text(self):
        return arcade.Text('KRACH!',150,150,arcade.color.WHITE)
        
    
class Hit_2():

    def __init__(self, spieler: Spieler):
        self.spieler = spieler

    def hit_text(self):
        return arcade.Text('Autschi',150,150,arcade.color.WHITE)
        
    
class Hit_3():

    def __init__(self, spieler: Spieler):
        self.spieler = spieler

    def hit_text(self):
        return arcade.Text('BOOM BOOM BOOM',150,150,arcade.color.WHITE)
    
class Hit_4():

    def __init__(self, spieler: Spieler):
        self.spieler = spieler

    def hit_text(self):
        return arcade.Text('Katsching',150,150,arcade.color.WHITE)
    



# 2. spieler inputs 
# runde gewonnen -> zurücksetzen der arena und zähler aus 1 : 0
# Spiel gewonnen -> 2 von 3 runden gewonnen -> Spiel gewonnen schriftzug und spiel zurücksetzen
# draw verschiedene textnachrichten über spieler wenn spieler gehittet (Protokoll)   


         

    

            


    