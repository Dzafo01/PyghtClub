import arcade
from arcade import Window

from eingabefilter import EingabeFilter
from arena import Arena


class GameEngine(Window):
    """
    GameEngine ist das Hauptspielfenster und die Engine, die das Spiel ausführt.
    
    Attribute:
        breite (int): Die Breite des Spielfensters.
        hoehe (int): Die Höhe des Spielfensters.
        welt (Arena): Die Spielwelt oder Arena, in der das Spiel stattfindet.
        eingabefilter (EingabeFilter): Der Eingabefilter zur Verwaltung der Benutzereingaben.
    """

    def __init__(self, breite: int = 600, hoehe: int = 600):
        """
        Initialisiert die Spielengine mit einem Fenster der angegebenen Breite und Höhe.

        Args:
            breite (int): Die Breite des Spielfensters. Standard ist 600.
            hoehe (int): Die Höhe des Spielfensters. Standard ist 600.
        """
        super().__init__(breite, hoehe)
        self.breite = breite
        self.hoehe = hoehe
        self.eingabefilter = EingabeFilter()
        self.welt = Arena(breite, hoehe)

        #self.background = None  

    # def setup(self):
    #      """
    #      Richten Sie das Spiel ein, einschließlich Laden von Ressourcen wie dem Hintergrundbild.
    #      """
    #      self.background = arcade.load_texture("Bilder/Hintergrund.jpg")

    def on_update(self, delta_time: float):
        """
        Aktualisiert den Spielzustand.

        Args:
            delta_time (float): Die Zeit, die seit dem letzten Update vergangen ist.
        """
        self.eingabefilter.on_update()
        self.welt.update(delta_time)

    def on_draw(self):
        """
        Rendert den Spielbildschirm.
        """
        arcade.start_render()
        self.welt.zeichne()
        #arcade.draw_lrwh_rectangle_textured(0, 0, self.breite, self.hoehe, self.background)

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Behandelt Tastendruckereignisse.

        Args:
            symbol (int): Die Taste, die gedrückt wurde.
            modifiers (int): Modifikatoren, die während des Tastendrucks aktiv waren.
        """
        self.eingabefilter.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        """
        Behandelt Tastenfreigabeereignisse.

        Args:
            symbol (int): Die Taste, die losgelassen wurde.
            modifiers (int): Modifikatoren, die während der Tastenfreigabe aktiv waren.
        """
        self.eingabefilter.on_key_release(symbol, modifiers)


game = GameEngine()
game.run()
