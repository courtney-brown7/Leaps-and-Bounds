import arcade

SCREEN_HEIGHT = 650
SCREEN_WIDTH = 1000
SCREEN_TITLE = 'Mountain Level'

class Level2View(arcade.View):
    def __init__(self):
        super().__init__()

        self.background = None

    def setup(self):
        self.background = arcade.load_texture("backgrounds/nature.jpg")
def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    level_2_view = Level2View()
    level_2_view.setup()
    window.show_view(level_2_view)
    arcade.run()



if __name__ == "__main__":
    main()