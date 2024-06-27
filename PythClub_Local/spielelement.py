# standard
from abc import ABC, abstractmethod
import math

class SpielElement(ABC):
    x: float
    y: float
    speed_x: int
    speed_y: int
    is_jump_active: bool
    
    

    def __init__(
        self, x: float, y: float, speed_x: float, speed_y: float
    ) -> None:
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        
        

    def update(self, delta_time: float):
        self.x += self.speed_x
        self.y += self.speed_y

    


 

    @abstractmethod
    def zeichne(self): ...