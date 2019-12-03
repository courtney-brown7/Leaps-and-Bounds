import arcade


class Level2View(arcade.View):
    def __init__(self):
        super().__init__()

        self.background = None

    def setup(self):
        self.background = arcade.load_texture("backgrounds/nature.jpg")
