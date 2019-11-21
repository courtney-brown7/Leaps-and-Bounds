import arcade

SCREEN_HEIGHT = 650
SCREEN_WIDTH = 1000
SCREEN_TITLE = 'Endless Stairs'
CHARACTER_SCALING = .05
TILE_SCALING = .08
COIN_SCALING = .5

# movement
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 17

# scrolling
TOP_VIEWPORT_MARGIN = 100


class GameWindow(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.background = None
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.player_sprite = None
        self.physics_engine = None

        self.view_bottom = 0
        self.view_left = 0

        self.collect_coin_sound = arcade.load_sound("sprite/coin5.wav")
        self.jump_sound = arcade.load_sound("sprite/jump4.wav")

    def setup(self):
        self.background = arcade.load_texture("backgrounds/beach.png")
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("sprite/chicken.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 120
        self.player_list.append(self.player_sprite)

        for x in range(0, 1250, 64):
            wall = arcade.Sprite("sprite/sand.jpg", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        for x in range(128, 1250, 256):
            coin = arcade.Sprite("sprite/coinGold.png", COIN_SCALING)
            coin.center_x = x
            coin.center_y = 96
            self.coin_list.append(coin)

        coordinate_list = [[256, 96],
                           [430, 200],
                           [870, 380],
                           [650, 300]
                           ]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("sprite/seashell.png", TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player_list.draw()
        self.coin_list.draw()
        self.wall_list.draw()

    def on_key_press(self, key, modifiers):
        # jump
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)

        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        self.physics_engine.update()

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)


        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)

        # scrolling up boundary
        changed = False
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        if changed:
            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = GameWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
