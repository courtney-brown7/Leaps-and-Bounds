import arcade
import random

from Level import LevelView
from final_slide import FinalView

TILE_SCALING = .08
SPRITE_SCALING = 0.2
SCREEN_HEIGHT = 650
SCREEN_WIDTH = 1000
SCREEN_TITLE = 'Space Level'
GRAVITY = .7


class FallingStars(arcade.Sprite):
    """ Simple sprite that falls down """

    def update(self):
        """ Move the coin """

        # Fall down
        self.center_y -= 2

        # Did we go off the screen? If so, pop back to the top.
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT


class Level3View(LevelView):
    def __init__(self):
        super().__init__()

        self.wall_list = None

        arcade.set_background_color(arcade.color.BLACK)

    def falling_stars(self):
        for i in range(30):
            # Create the coin instance
            coin = FallingStars("sprite/star.png", SPRITE_SCALING / 2)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("sprite/ufo.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.score = 0
        for x in range(0, 1250, 64):
            wall = arcade.Sprite("sprite/sand.jpg", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        self.falling_stars()
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list,
                                                             GRAVITY)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_sprite.draw()
        self.coin_list.draw()

        # Put the text on the screen.
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.WHITE, 18)

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.physics_engine.update()

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        if self.score == 30:
            final_view = FinalView()
            self.window.show_view(final_view)

def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    level_3_view = Level3View()
    level_3_view.setup()
    window.show_view(level_3_view)
    arcade.run()


if __name__ == "__main__":
    main()
