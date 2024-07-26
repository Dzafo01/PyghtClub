# standard
from abc import ABC, abstractmethod

class SpielElement(ABC):
    x: float
    y: float
    height: float
    width : float
    
    

    def __init__(
        self, x: float, y: float,  height:float,width:float
    ) -> None:
        self.x = x
        self.y = y 
        self.height = height
        self.width = width  
       
        
        

    def update(self, delta_time: float):
        ...
      
    def hat_kollision(self, elem: 'SpielElement') -> bool:
        return (abs(self.x - elem.x)< self.width) & (abs(self.y - elem.y)<self.height)

    @abstractmethod
    def on_collision(self, elem: 'SpielElement'):
            ...


    


 

    @abstractmethod
    def zeichne(self): ...