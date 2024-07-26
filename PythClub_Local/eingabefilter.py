# vendor
from arcade import key

# custom
from messages import NeueUserEingabe_P1, NeueUserEingabe_P2
from messages import UserEingabe
from message_queue import message_queue as mq



class EingabeFilter:
    """
    Die EingabeFilter-Klasse verwaltet die Benutzereingaben und übersetzt sie in Spielaktionen.

    Attribute:
        bewegungstasten_p1 (Dict[int, bool]): Ein Wörterbuch, das den Zustand der Bewegungstasten für Spieler 1 speichert.
        bewegungstasten_p2 (Dict[int, bool]): Ein Wörterbuch, das den Zustand der Bewegungstasten für Spieler 2 speichert.
    """

    def __init__(self):
        """
        Initialisiert die Bewegungstasten für Spieler 1 und Spieler 2.
        """
        self.bewegungstasten_p1 = {taste: False for taste in [key.A, key.D, key.S, key.R, key.T]}  # neu
        self.bewegungstasten_p2 = {taste: False for taste in [key.J, key.L, key.K, key.I, key.U, key.Z]}

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Verarbeitet Tastendruckereignisse und fügt die entsprechenden Aktionen zur Nachrichtenwarteschlange hinzu.

        Args:
            symbol (int): Der Schlüsselcode der gedrückten Taste.
            modifiers (int): Modifikatoren, die während des Tastendrucks aktiv waren.
        """
        if symbol == key.W:
            mq.queue(NeueUserEingabe_P1(UserEingabe.SPRINGEN_P1))
        if symbol == key.S:
            mq.queue(NeueUserEingabe_P1(UserEingabe.DUCKEN_P1))
        if symbol == key.R:
            mq.queue(NeueUserEingabe_P1(UserEingabe.PUNCH_P1))  ## neu
        if symbol == key.T:
            mq.queue(NeueUserEingabe_P1(UserEingabe.KICK_P1))
        if symbol == key.I:
            mq.queue(NeueUserEingabe_P2(UserEingabe.SPRINGEN_P2))
        if symbol == key.K:
            mq.queue(NeueUserEingabe_P2(UserEingabe.DUCKEN_P2))
        if symbol == key.U:
            mq.queue(NeueUserEingabe_P2(UserEingabe.PUNCH_P2))  ## neu
        if symbol == key.Z:
            mq.queue(NeueUserEingabe_P2(UserEingabe.KICK_P2))
        if symbol in self.bewegungstasten_p1:
            self.bewegungstasten_p1[symbol] = True
        if symbol in self.bewegungstasten_p2:
            self.bewegungstasten_p2[symbol] = True

    def on_key_release(self, symbol: int, modifiers: int):
        """
        Verarbeitet Tastenfreigabeereignisse und fügt die entsprechenden Aktionen zur Nachrichtenwarteschlange hinzu.

        Args:
            symbol (int): Der Schlüsselcode der freigegebenen Taste.
            modifiers (int): Modifikatoren, die während der Tastenfreigabe aktiv waren.
        """
        if symbol in self.bewegungstasten_p1:
            self.bewegungstasten_p1[symbol] = False
            mq.queue(NeueUserEingabe_P1(UserEingabe.KEINE_EINGABE_P1))
        if symbol in self.bewegungstasten_p2:
            self.bewegungstasten_p2[symbol] = False
            mq.queue(NeueUserEingabe_P2(UserEingabe.KEINE_EINGABE_P2))

    def on_update(self) -> None:
        """
        Aktualisiert den Zustand der Bewegungstasten und fügt die entsprechenden Bewegungsaktionen zur Nachrichtenwarteschlange hinzu.
        """
        if self.bewegungstasten_p1[key.A] and not self.bewegungstasten_p1[key.D]:
            mq.queue(NeueUserEingabe_P1(UserEingabe.LINKS_P1))
        elif self.bewegungstasten_p1[key.D] and not self.bewegungstasten_p1[key.A]:
            mq.queue(NeueUserEingabe_P1(UserEingabe.RECHTS_P1))
        if self.bewegungstasten_p2[key.J] and not self.bewegungstasten_p2[key.L]:
            mq.queue(NeueUserEingabe_P2(UserEingabe.LINKS_P2))
        elif self.bewegungstasten_p2[key.L] and not self.bewegungstasten_p2[key.J]:
            mq.queue(NeueUserEingabe_P2(UserEingabe.RECHTS_P2))

        # if self.bewegungstasten_p2[key.P]:
        #     mq.queue(NeueUserEingabe(UserEingabe.PUNCH_P2))    ## neu
        # if self.bewegungstasten_p2[key.Z]:
        #     mq.queue(NeueUserEingabe(UserEingabe.KICK_P2))
