# standard
from typing import Protocol
import random

# vendor
import arcade
#from arcade import color

# custom
from spielelement import SpielElement
from message_queue import message_queue as mq
from messages import NeueUserEingabe_P1, NeueUserEingabe_P2, UserEingabe
from interfaces import Temporaer, Permanent

class Spieler(SpielElement):
    """
    Die Spieler-Klasse repräsentiert einen Spieler im Spiel und verwaltet dessen Zustand und Aktionen.

    Attribute:
        health (float): Die Gesundheit des Spielers.
        speed_x (float): Die horizontale Geschwindigkeit des Spielers.
        speed_y (float): Die vertikale Geschwindigkeit des Spielers.
        cooldown (float): Die Abklingzeit für Angriffe.
        on_cooldown (bool): Gibt an, ob der Spieler derzeit eine Abklingzeit hat.
        timer (float): Der Timer für das Spiel.
        player (int): Die Spielernummer (1 oder 2).
        standing_texture (arcade.Texture): Die Textur, die angezeigt wird, wenn der Spieler steht.
        punching_texture (arcade.Texture): Die Textur, die angezeigt wird, wenn der Spieler schlägt.
        kicking_texture (arcade.Texture): Die Textur, die angezeigt wird, wenn der Spieler tritt.
        current_texture (arcade.Texture): Die aktuelle Textur des Spielers.
        standing_texture_spiegel (arcade.Texture): Die gespiegelte Textur, die angezeigt wird, wenn der Spieler steht.
        punching_texture_spiegel (arcade.Texture): Die gespiegelte Textur, die angezeigt wird, wenn der Spieler schlägt.
        kicking_texture_spiegel (arcade.Texture): Die gespiegelte Textur, die angezeigt wird, wenn der Spieler tritt.
        current_texture_spiegel (arcade.Texture): Die gespiegelte aktuelle Textur des Spielers.
    """

    def __init__(self, x: float, y: float, player: int) -> None:
        """
        Initialisiert einen neuen Spieler.

        Args:
            x (float): Die x-Koordinate des Spielers.
            y (float): Die y-Koordinate des Spielers.
            player (int): Die Spielernummer (1 oder 2).
        """
        super().__init__(x, y, 80, 40)
        self.attack = Attack(self)  # neu
        self.health = 100
        self.speed_x = 0
        self.speed_y = 0
        self.cooldown = 0
        self.on_cooldown = True
        self.timer = 30
        self.player = player

        self.standing_texture = arcade.load_texture("Bilder/Stehen.png")
        self.punching_texture = arcade.load_texture("Bilder/Schlagen.png")
        self.kicking_texture = arcade.load_texture("Bilder/Treten.png")
        self.standing_texture_spiegel = arcade.load_texture("Bilder/Stehen_gedreht.png")
        self.punching_texture_spiegel = arcade.load_texture("Bilder/Schlagen_gedreht.png")
        self.kicking_texture_spiegel = arcade.load_texture("Bilder/Treten_gedreht.png")

        if self.player == 1:
            self.current_texture = self.standing_texture
        if self.player == 2:
            self.current_texture = self.standing_texture_spiegel

    def setup(self):
        """
        Setzt die Attribute des Spielers zurück.
        """
        self.health = 100
        self.speed_x = 0
        self.speed_y = 0
        self.cooldown = 0
        self.on_cooldown = True
        self.player_dead = False
        self.timer = 30

    def zeichne_healthbar_P1(self):
        """
        Zeichnet die Gesundheitsleiste für Spieler 1.
        """
        ratio = self.health / 100
        if self.health < 0:
           ratio = 0
        arcade.draw_xywh_rectangle_filled(49, 499, 202, 32, arcade.color.WHITE)
        arcade.draw_xywh_rectangle_filled(50, 500, 200 * ratio, 30, arcade.color.RED)  # Pfusch Lösung

    def zeichne_name_P1(self):
        """
        Zeichnet den Namen für Spieler 1.
        """
        arcade.draw_text("Player 1", 150, 475, arcade.color.WHITE, font_size=20, anchor_x="center", anchor_y="center")

    def zeichne_name_P2(self):
        """
        Zeichnet den Namen für Spieler 2.
        """
        arcade.draw_text("Player 2", 450, 475, arcade.color.WHITE, font_size=20, anchor_x="center", anchor_y="center")

    def zeichne_healthbar_P2(self):
        """
        Zeichnet die Gesundheitsleiste für Spieler 2.
        """
        ratio = self.health / 100
        if self.health < 0:
            ratio = 0
        arcade.draw_xywh_rectangle_filled(349, 499, 202, 32, arcade.color.WHITE)
        arcade.draw_xywh_rectangle_filled(350, 500, 200 * ratio, 30, arcade.color.RED)

    def zeichne_timer(self):
        """
        Zeichnet den Timer.
        """
        seconds = int(self.timer) % 60
        timer_text = f"{seconds:02d}"
        arcade.draw_text(timer_text, 300, 510, arcade.color.WHITE, 20, anchor_x="center")

    def set_texture(self, action: str):
        """
        Setzt die Textur des Spielers basierend auf der Aktion.

        Args:
            action (str): Die Aktion, die der Spieler ausführt (stehen, schlagen, treten, stehen_spiegel, schlagen_spiegel, treten_spiegel).
        """
        if action == "stehen":
            self.current_texture = self.standing_texture
        elif action == "schlagen":
            self.current_texture = self.punching_texture
        elif action == "treten":
            self.current_texture = self.kicking_texture

        elif action == "stehen_spiegel":
            self.current_texture = self.kicking_texture_spiegel
        elif action == "schlagen_spiegel":
            self.current_texture = self.punching_texture_spiegel
        elif action == "treten_spiegel":
            self.current_texture = self.kicking_texture_spiegel

    def zeichne(self):
        """
        Zeichnet den Spieler und seine Attribute (Gesundheitsleiste, Timer, Name).
        """
        arcade.draw_texture_rectangle(self.x, self.y + 40, self.width, self.height, self.current_texture)
        self.attack.zeichne()
        if self.player == 1:
            self.zeichne_healthbar_P1()
        elif self.player == 2:
            self.zeichne_healthbar_P2()
        self.zeichne_timer()
        self.zeichne_name_P1()
        self.zeichne_name_P2()

    def update(self, delta_time: float):
        """
        Aktualisiert den Zustand des Spielers basierend auf Benutzereingaben und der Zeit.

        Args:
            delta_time (float): Die verstrichene Zeit seit dem letzten Update.
        """
        if self.player == 1:
            for message in mq.popAll("NEUE_USER_EINGABE_P1"):
                if isinstance(message, NeueUserEingabe_P1):
                    if message.ereignis == UserEingabe.SPRINGEN_P1:
                        self.springen()
                    elif message.ereignis == UserEingabe.DUCKEN_P1:
                        self.ducken()
                    else:
                        self.height = 80
                    if message.ereignis == UserEingabe.LINKS_P1:
                        self.beschleunige_x_neg()
                    elif message.ereignis == UserEingabe.RECHTS_P1:
                        self.beschleunige_x_pos()
                    elif message.ereignis == UserEingabe.KEINE_EINGABE_P1:
                        self.speed_x = 0
                    elif message.ereignis == UserEingabe.PUNCH_P1:  # neu
                        self.attack.punch()
                        self.on_cooldown = False
                        self.set_texture("schlagen")
                    elif message.ereignis == UserEingabe.KICK_P1:  # neu
                        self.attack.kick()
                        self.on_cooldown = False
                        self.set_texture("treten")
                    else:
                        self.set_texture("stehen")
        if self.player == 2:
            for message in mq.popAll("NEUE_USER_EINGABE_P2"):
                if isinstance(message, NeueUserEingabe_P2):
                    if message.ereignis == UserEingabe.SPRINGEN_P2:
                        self.springen()
                    elif message.ereignis == UserEingabe.DUCKEN_P2:
                        self.ducken()
                    else:
                        self.height = 80
                    if message.ereignis == UserEingabe.LINKS_P2:
                        self.beschleunige_x_neg()
                    elif message.ereignis == UserEingabe.RECHTS_P2:
                        self.beschleunige_x_pos()
                    elif message.ereignis == UserEingabe.KEINE_EINGABE_P2:
                        self.speed_x = 0
                    elif message.ereignis == UserEingabe.PUNCH_P2:  # neu
                        self.attack.punch()
                        self.on_cooldown = False
                        self.set_texture("schlagen_spiegel")
                    elif message.ereignis == UserEingabe.KICK_P2:  # neu
                        self.attack.kick()
                        self.on_cooldown = False
                        self.set_texture("treten_spiegel")
                    else:
                        self.set_texture("stehen_spiegel")
        self.y += self.speed_y
        self.x += self.speed_x
        if self.on_cooldown == False:
            self.cooldown += 1
        if self.cooldown > 40:
            self.cooldown = 0
            self.on_cooldown = True
            self.set_texture("stehen")

        self.timer -= delta_time
        if self.timer <= 0:
            self.timer = 0
            self.reset_fighter()

    def beschleunige_x_pos(self):
        """
        Beschleunigt den Spieler nach rechts.
        """
        self.x += 5

    def beschleunige_x_neg(self):
        """
        Beschleunigt den Spieler nach links.
        """
        self.x -= 5

    def springen(self):
        """
        Lässt den Spieler springen.
        """
        self.speed_y += 15

    def ducken(self):
        """
        Lässt den Spieler sich ducken.
        """
        self.height = 40

    def __repr__(self) -> str:
        """
        Gibt eine string-Repräsentation des Spielers zurück.

        Returns:
            str: Die string-Repräsentation des Spielers.
        """
        return "Spieler (%.0f/%.0f)" % (self.x, self.y)

    def on_collision(self, elem: 'SpielElement'):
        """
        Wird aufgerufen, wenn der Spieler mit einem anderen Spielelement kollidiert.

        Args:
            elem (SpielElement): Das andere Spielelement.
        """
        if isinstance(elem, Permanent):
            self.x = elem.x - elem.width

    def reset_fighter(self):
        """
        Setzt den Zustand des Kämpfers zurück und zeichnet ihn neu.
        """
        self.setup()
        self.zeichne()

class Attack(SpielElement):
    """
    Die Attack-Klasse repräsentiert eine Angriffshandlung eines Spielers.

    Attribute:
        is_left (bool): Gibt an, ob der Angriff nach links geht.
        text (Hit_Text): Der Text, der bei einem Treffer angezeigt wird.
    """

    def __init__(self, spieler: Spieler):
        """
        Initialisiert einen neuen Angriff.

        Args:
            spieler (Spieler): Der Spieler, der den Angriff ausführt.
        """
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
        """
        Führt einen Schlag aus.
        """
        if self.spieler.on_cooldown == True:  # neu
            self.is_punching = True

    def kick(self):
        """
        Führt einen Tritt aus.
        """
        if self.spieler.on_cooldown == True:  # neu
            self.is_kicking = True

    def shuffle_text(self):
        """
        Wählt zufällig einen Treffertext aus.

        Returns:
            str: Der ausgewählte Treffertext.
        """
        rand = random.choice([Hit.hit_text(self), Hit_2.hit_text(self), Hit_3.hit_text(self), Hit_4.hit_text(self)])
        return rand

    def on_collision(self, elem: 'Spieler'):
        """
        Wird aufgerufen, wenn der Angriff einen Spieler trifft.

        Args:
            elem (Spieler): Der getroffene Spieler.
        """
        if elem != self.spieler:
            elem.health -= 10
            # self.text = self.shuffle_text()

    def zeichne(self):
        """
        Zeichnet den Angriff.
        """
        if (self.is_left):
            self.x = self.spieler.x + self.spieler.width
        else:
            self.x = self.spieler.x - self.spieler.width
        if self.is_punching:
            arcade.draw_xywh_rectangle_outline(self.x, self.spieler.y + self.spieler.height / 2, self.spieler.width, self.spieler.height / 2, arcade.color.BLACK)
            self.is_punching = False  # Reset after drawing
        if self.is_kicking:
            arcade.draw_xywh_rectangle_outline(self.x, self.spieler.y, self.spieler.width, self.spieler.height / 2, arcade.color.BLACK)
            self.is_kicking = False  # Reset after drawing
        # if self.hat_kollision():
        #     self.text.draw()

class Hit_Text(Protocol):
    """
    Protokoll für Treffertexte.
    """
    def hit_text(self) -> None:
        """
        Gibt den Treffertext zurück.
        """
        raise NotImplementedError

class Hit():
    """
    Klasse für Treffertext "KRACH!".
    """

    def __init__(self, spieler: Spieler):
        """
        Initialisiert den Treffertext.

        Args:
            spieler (Spieler): Der Spieler, der den Treffertext anzeigt.
        """
        self.spieler = spieler

    def hit_text(self):
        """
        Gibt den Treffertext zurück.

        Returns:
            arcade.Text: Der Treffertext.
        """
        return arcade.Text('KRACH!', 150, 150, arcade.color.WHITE)

class Hit_2():
    """
    Klasse für Treffertext "Autschi".
    """

    def __init__(self, spieler: Spieler):
        """
        Initialisiert den Treffertext.

        Args:
            spieler (Spieler): Der Spieler, der den Treffertext anzeigt.
        """
        self.spieler = spieler

    def hit_text(self):
        """
        Gibt den Treffertext zurück.

        Returns:
            arcade.Text: Der Treffertext.
        """
        return arcade.Text('Autschi', 150, 150, arcade.color.WHITE)

class Hit_3():
    """
    Klasse für Treffertext "BOOM BOOM BOOM".
    """

    def __init__(self, spieler: Spieler):
        """
        Initialisiert den Treffertext.

        Args:
            spieler (Spieler): Der Spieler, der den Treffertext anzeigt.
        """
        self.spieler = spieler

    def hit_text(self):
        """
        Gibt den Treffertext zurück.

        Returns:
            arcade.Text: Der Treffertext.
        """
        return arcade.Text('BOOM BOOM BOOM', 150, 150, arcade.color.WHITE)

class Hit_4():
    """
    Klasse für Treffertext "Katsching".
    """

    def __init__(self, spieler: Spieler):
        """
        Initialisiert den Treffertext.

        Args:
            spieler (Spieler): Der Spieler, der den Treffertext anzeigt.
        """
        self.spieler = spieler

    def hit_text(self):
        """
        Gibt den Treffertext zurück.

        Returns:
            arcade.Text: Der Treffertext.
        """
        return arcade.Text('Katsching', 150, 150, arcade.color.WHITE)


# 2. spieler inputs 
# runde gewonnen -> zurücksetzen der arena und zähler aus 1 : 0
# Spiel gewonnen -> 2 von 3 runden gewonnen -> Spiel gewonnen schriftzug und spiel zurücksetzen
# draw verschiedene textnachrichten über spieler wenn spieler gehittet (Protokoll)   