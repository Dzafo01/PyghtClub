from typing import Protocol
import arcade
from spieler import Spieler

class Hit_Text(Protocol):
    """
    Ein Protokoll, das die Methode definiert, die eine Treffertextdarstellung bereitstellt.

    Dieses Protokoll beschreibt ein Objekt, das die Methode `hit_text` bereitstellt.
    Objekte, die dieses Protokoll implementieren, müssen die `hit_text`-Methode implementieren.

    Methoden:
        hit_text() -> None:
            Gibt eine visuelle Darstellung eines Treffertextes aus.
            Muss von Klassen implementiert werden, die dieses Protokoll erfüllen.
    """

    def hit_text(self) -> None:
        """
        Gibt eine visuelle Darstellung eines Treffertextes aus.

        Diese Methode ist abstrakt und muss von Klassen implementiert werden, 
        die dieses Protokoll erfüllen.

        Raises:
            NotImplementedError: Wenn die Methode nicht von der implementierenden Klasse überschrieben wird.
        """
        raise NotImplementedError

class Hit():
    """
    Eine Klasse zur Darstellung eines Treffertextes mit dem Text 'Hit'.

    Diese Klasse implementiert das `Hit_Text`-Protokoll und zeichnet den Treffertext 'Hit' an der Position des Spielers.

    Attribute:
        spieler (Spieler): Der Spieler, an dessen Position der Treffertext angezeigt wird.
    
    Methoden:
        hit_text() -> None:
            Zeichnet den Treffertext 'Hit' an der Position des Spielers.
    """

    def __init__(self, spieler: Spieler):
        """
        Initialisiert ein neues Hit-Objekt.

        Args:
            spieler (Spieler): Der Spieler, an dessen Position der Treffertext angezeigt wird.
        """
        self.spieler = spieler

    def hit_text(self) -> None:
        """
        Zeichnet den Treffertext 'Hit' an der Position des Spielers.

        Verwendet die `arcade.draw_text`-Funktion, um den Text 'Hit' in blauer Farbe an der Position des Spielers darzustellen.
        """
        arcade.draw_text('Hit', self.spieler.x, self.spieler.y, arcade.color.ALICE_BLUE)

class Hit_2():
    """
    Eine Klasse zur Darstellung eines Treffertextes mit dem Text 'Pow'.

    Diese Klasse implementiert das `Hit_Text`-Protokoll und zeichnet den Treffertext 'Pow' an der Position des Spielers.

    Attribute:
        spieler (Spieler): Der Spieler, an dessen Position der Treffertext angezeigt wird.
    
    Methoden:
        hit_text() -> None:
            Zeichnet den Treffertext 'Pow' an der Position des Spielers.
    """

    def __init__(self, spieler: Spieler):
        """
        Initialisiert ein neues Hit_2-Objekt.

        Args:
            spieler (Spieler): Der Spieler, an dessen Position der Treffertext angezeigt wird.
        """
        self.spieler = spieler

    def hit_text(self) -> None:
        """
        Zeichnet den Treffertext 'Pow' an der Position des Spielers.

        Verwendet die `arcade.draw_text`-Funktion, um den Text 'Pow' in blauer Farbe an der Position des Spielers darzustellen.
        """
        arcade.draw_text('Pow', self.spieler.x, self.spieler.y, arcade.color.ALICE_BLUE)

class Hit_3():
    """
    Eine Klasse zur Darstellung eines Treffertextes mit dem Text 'Boom'.

    Diese Klasse implementiert das `Hit_Text`-Protokoll und zeichnet den Treffertext 'Boom' an der Position des Spielers.

    Attribute:
        spieler (Spieler): Der Spieler, an dessen Position der Treffertext angezeigt wird.
    
    Methoden:
        hit_text() -> None:
            Zeichnet den Treffertext 'Boom' an der Position des Spielers.
    """

    def __init__(self, spieler: Spieler):
        """
        Initialisiert ein neues Hit_3-Objekt.

        Args:
            spieler (Spieler): Der Spieler, an dessen Position der Treffertext angezeigt wird.
        """
        self.spieler = spieler

    def hit_text(self) -> None:
        """
        Zeichnet den Treffertext 'Boom' an der Position des Spielers.

        Verwendet die `arcade.draw_text`-Funktion, um den Text 'Boom' in blauer Farbe an der Position des Spielers darzustellen.
        """
        arcade.draw_text('Boom', self.spieler.x, self.spieler.y, arcade.color.ALICE_BLUE)

class Hit_4():
    """
    Eine Klasse zur Darstellung eines Treffertextes mit dem Text 'Hua'.

    Diese Klasse implementiert das `Hit_Text`-Protokoll und zeichnet den Treffertext 'Hua' an der Position des Spielers.

    Attribute:
        spieler (Spieler): Der Spieler, an dessen Position der Treffertext angezeigt wird.
    
    Methoden:
        hit_text() -> None:
            Zeichnet den Treffertext 'Hua' an der Position des Spielers.
    """

    def __init__(self, spieler: Spieler):
        """
        Initialisiert ein neues Hit_4-Objekt.

        Args:
            spieler (Spieler): Der Spieler, an dessen Position der Treffertext angezeigt wird.
        """
        self.spieler = spieler

    def hit_text(self) -> None:
        """
        Zeichnet den Treffertext 'Hua' an der Position des Spielers.

        Verwendet die `arcade.draw_text`-Funktion, um den Text 'Hua' in blauer Farbe an der Position des Spielers darzustellen.
        """
        arcade.draw_text('Hua', self.spieler.x, self.spieler.y, arcade.color.ALICE_BLUE)
