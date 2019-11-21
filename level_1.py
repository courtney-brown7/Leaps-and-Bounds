import arcade
from arcade.examples.sprite_move_animation import CHARACTER_SCALING

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 400
SCREEN_TITLE = 'Endless Stairs'


class GameWindow(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.background = None

    def setup(self):
        self.background = arcade.load_texture("backgrounds/beach.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)


class Sprite(arcade.Sprite):
    def __init__(self):
        self.player_list = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("", CHARACTER_SCALING)


def main():
    """ Main method """
    window = GameWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
