import arcade

from Level import LevelView
from level_2 import Level2View

SCREEN_HEIGHT = 650
SCREEN_WIDTH = 1000
SCREEN_TITLE = 'Sea Level'
CHARACTER_SCALING = .1
TILE_SCALING = .08
COIN_SCALING = .5

# movement
GRAVITY = 1
# scrolling
TOP_VIEWPORT_MARGIN = 100


class Level1View(LevelView):

    def __init__(self):
        super().__init__()



    def setup(self):
        self.background = arcade.load_texture("backgrounds/beach.png")
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("sprite/crab.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 120
        self.player_list.append(self.player_sprite)

        self.score = 0

        """ places the sand down as the floor """
        for x in range(0, 1250, 64):
            wall = arcade.Sprite("sprite/sand.jpg", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        """using the coordinate list, places the seashells and the 
        coins above it. """
        coordinate_list = [[256, 96],
                           [430, 200],
                           [870, 380],
                           [650, 300]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("sprite/seashell.png", TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)
            coin = arcade.Sprite("sprite/coinGold.png", COIN_SCALING)
            coin.center_x = coordinate[0]
            coin.center_y = coordinate[1] + 70
            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list, GRAVITY)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player_list.draw()
        self.coin_list.draw()
        self.wall_list.draw()

        # coin display points
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.WHITE, 18)



    def on_update(self, delta_time):
        self.physics_engine.update()

        # collision with coins- If the coin hits the sprite
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)
            self.score += 1

        if self.score == 4:
            level_2_view = Level2View()
            level_2_view.setup()
            self.window.show_view(level_2_view)




def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    level_1_view = Level1View()
    level_1_view.setup()
    window.show_view(level_1_view)
    arcade.run()


if __name__ == "__main__":
    main()
