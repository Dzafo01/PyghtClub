#import math
from typing import List, Tuple

class PunktListe(List[Tuple[float, float]]):
    """
    Eine Klasse, die eine Liste von Punkten (Tupel von x- und y-Koordinaten) darstellt
    und um Methoden zur Manipulation dieser Punkte erweitert wird.

    Args:
        werte (List[Tuple[float, float]], optional): Eine Liste von Tupeln, die die Anfangswerte der Punkte darstellen.
    """
    
    def __init__(self, werte: List[Tuple[float, float]] = []) -> None:
        """
        Initialisiert eine neue PunktListe mit den gegebenen Werten.

        Args:
            werte (List[Tuple[float, float]], optional): Eine Liste von Tupeln, die die Anfangswerte der Punkte darstellen.
        """
        self.extend(werte)

    def verschiebe(self, dx: float, dy: float) -> "PunktListe":
        """
        Verschiebt alle Punkte in der PunktListe um die angegebenen x- und y-Werte.

        Args:
            dx (float): Der Wert, um den die x-Koordinaten verschoben werden sollen.
            dy (float): Der Wert, um den die y-Koordinaten verschoben werden sollen.

        Returns:
            PunktListe: Eine neue PunktListe mit den verschobenen Punkten.
        """
        neu = PunktListe()
        for x, y in self:
            neu.append((x + dx, y + dy))
        return neu
