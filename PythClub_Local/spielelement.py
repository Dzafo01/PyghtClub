from abc import ABC, abstractmethod



class SpielElement(ABC):
    """
    Die SpielElement-Klasse ist eine abstrakte Basisklasse für alle Spielelemente im Spiel.

    Attribute:
        x (float): Die x-Koordinate des Spielelements.
        y (float): Die y-Koordinate des Spielelements.
        height (float): Die Höhe des Spielelements.
        width (float): Die Breite des Spielelements.
    """

    def __init__(self, x: float, y: float, height: float, width: float) -> None:
        """
        Initialisiert ein neues Spielelement.

        Args:
            x (float): Die x-Koordinate des Spielelements.
            y (float): Die y-Koordinate des Spielelements.
            height (float): Die Höhe des Spielelements.
            width (float): Die Breite des Spielelements.
        """
        self.x = x
        self.y = y 
        self.height = height
        self.width = width  

    def update(self, delta_time: float):
        """
        Aktualisiert den Zustand des Spielelements basierend auf der verstrichenen Zeit.

        Args:
            delta_time (float): Die verstrichene Zeit seit dem letzten Update.
        """
        ...

    def hat_kollision(self, elem: 'SpielElement') -> bool:
        """
        Überprüft, ob dieses Spielelement mit einem anderen Spielelement kollidiert.

        Args:
            elem (SpielElement): Das andere Spielelement.

        Returns:
            bool: True, wenn eine Kollision vorliegt, andernfalls False.
        """
        return (abs(self.x - elem.x) < self.width) & (abs(self.y - elem.y) < self.height)

    @abstractmethod
    def on_collision(self, elem: 'SpielElement'):
        """
        Wird aufgerufen, wenn dieses Spielelement mit einem anderen Spielelement kollidiert.

        Args:
            elem (SpielElement): Das andere Spielelement.
        """
        ...

    @abstractmethod
    def zeichne(self):
        """
        Zeichnet das Spielelement.
        """
        ...
