from enum import Enum
from message_queue import Message
from spielelement import SpielElement

class NeuesSpielElement(Message):
    """
    Eine Nachricht, die ein neues SpielElement enthält.

    Args:
        elem (SpielElement): Das SpielElement, das der Nachricht hinzugefügt wird.
    """

    elem: SpielElement

    def __init__(self, elem: SpielElement) -> None:
        """
        Initialisiert eine neue Instanz der Nachricht mit einem SpielElement.

        Args:
            elem (SpielElement): Das SpielElement, das der Nachricht hinzugefügt wird.
        """
        super().__init__('NEUES_SPIEL_ELEMENT')
        self.elem = elem

class NeueHitMessage(Message):
    """
    Eine Nachricht, die ein SpielElement enthält, das getroffen wurde.

    Args:
        elem (SpielElement): Das SpielElement, das getroffen wurde.
    """

    elem: SpielElement

    def __init__(self, elem: SpielElement) -> None:
        """
        Initialisiert eine neue Instanz der Nachricht mit einem SpielElement.

        Args:
            elem (SpielElement): Das SpielElement, das getroffen wurde.
        """
        super().__init__('NEUE_HIT_MESSAGE')
        self.elem = elem

class UserEingabe(Enum):
    """
    Enum zur Darstellung von Benutzer-Eingaben für zwei Spieler.
    
    Werte:
        SPRINGEN_P1 (0): Spieler 1 springt.
        DUCKEN_P1 (1): Spieler 1 duckt sich.
        LINKS_P1 (2): Spieler 1 bewegt sich nach links.
        RECHTS_P1 (3): Spieler 1 bewegt sich nach rechts.
        KEINE_EINGABE_P1 (4): Spieler 1 hat keine Eingabe gemacht.
        SPRINGEN_P2 (5): Spieler 2 springt.
        DUCKEN_P2 (6): Spieler 2 duckt sich.
        LINKS_P2 (7): Spieler 2 bewegt sich nach links.
        RECHTS_P2 (8): Spieler 2 bewegt sich nach rechts.
        KEINE_EINGABE_P2 (9): Spieler 2 hat keine Eingabe gemacht.
        PUNCH_P1 (10): Spieler 1 führt einen Punch aus.
        KICK_P1 (11): Spieler 1 führt einen Kick aus.
        PUNCH_P2 (12): Spieler 2 führt einen Punch aus.
        KICK_P2 (13): Spieler 2 führt einen Kick aus.
    """

    SPRINGEN_P1 = 0
    DUCKEN_P1 = 1
    LINKS_P1 = 2
    RECHTS_P1 = 3
    KEINE_EINGABE_P1 = 4
    SPRINGEN_P2 = 5
    DUCKEN_P2 = 6
    LINKS_P2 = 7
    RECHTS_P2 = 8
    KEINE_EINGABE_P2 = 9
    PUNCH_P1 = 10 # neu
    KICK_P1 = 11 # neu
    PUNCH_P2 = 12
    KICK_P2 = 13

class NeueUserEingabe_P1(Message):
    """
    Eine Nachricht, die eine Benutzer-Eingabe für Spieler 1 enthält.

    Args:
        ereignis (UserEingabe): Das Ereignis, das die Eingabe für Spieler 1 beschreibt.
    """

    ereignis: UserEingabe

    def __init__(self, ereignis: UserEingabe) -> None:
        """
        Initialisiert eine neue Instanz der Nachricht mit einem Benutzer-Eingabe-Ereignis für Spieler 1.

        Args:
            ereignis (UserEingabe): Das Ereignis, das die Eingabe für Spieler 1 beschreibt.
        """
        super().__init__('NEUE_USER_EINGABE_P1')
        self.ereignis = ereignis

class NeueUserEingabe_P2(Message):
    """
    Eine Nachricht, die eine Benutzer-Eingabe für Spieler 2 enthält.

    Args:
        ereignis (UserEingabe): Das Ereignis, das die Eingabe für Spieler 2 beschreibt.
    """

    ereignis: UserEingabe

    def __init__(self, ereignis: UserEingabe) -> None:
        """
        Initialisiert eine neue Instanz der Nachricht mit einem Benutzer-Eingabe-Ereignis für Spieler 2.

        Args:
            ereignis (UserEingabe): Das Ereignis, das die Eingabe für Spieler 2 beschreibt.
        """
        super().__init__('NEUE_USER_EINGABE_P2')
        self.ereignis = ereignis
