import arcade

SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 650
SCREEN_TITLE = 'Endless Stairs'


class GameWindow(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.background = None

    def setup(self):
        self.background = arcade.load_texture("backgrounds/beach.png")
