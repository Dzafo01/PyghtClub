import arcade
from arcade import Window

from eingabefilter import EingabeFilter
from arena import Arena





class GameEngine(Window):

    breite: int
    hoehe: int
    welt: Arena

    eingabefilter: EingabeFilter

    def __init__(self, breite: int = 600, hoehe: int = 600):
        super().__init__(breite, hoehe)
        self.breite = breite
        self.hoehe = hoehe
        self.eingabefilter = EingabeFilter()
        self.welt = Arena(breite, hoehe)

    def on_update(self, delta_time: float):
        self.eingabefilter.on_update()
        self.welt.update(delta_time)

    def on_draw(self):
        arcade.start_render()
        self.welt.zeichne()

    def on_key_press(self, symbol: int, modifiers: int):
        self.eingabefilter.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        self.eingabefilter.on_key_release(symbol, modifiers)


game = GameEngine()
game.run()

