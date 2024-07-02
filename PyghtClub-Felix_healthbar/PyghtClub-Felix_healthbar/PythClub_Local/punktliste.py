import math
from typing import List
from typing import Tuple

class PunktListe(List[Tuple[float, float]]):
    def __init__(self, werte: List[Tuple[float, float]] = []) -> None:
        self.extend(werte)


    def verschiebe(self, dx: float, dy: float) -> "PunktListe":
        neu = PunktListe()
        for x, y in self:
            neu.append((x + dx, y + dy))
        return neu