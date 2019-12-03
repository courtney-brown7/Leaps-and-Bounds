import arcade
SPRITE_SCALING = 0.5
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
SCREEN_TITLE = 'Mountain Level'
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALING)

VIEWPORT_MARGIN = SPRITE_PIXEL_SIZE * SPRITE_SCALING
RIGHT_MARGIN = 4 * SPRITE_PIXEL_SIZE * SPRITE_SCALING


MOVEMENT_SPEED = 10 * SPRITE_SCALING
JUMP_SPEED = 28 * SPRITE_SCALING
GRAVITY = .9 * SPRITE_SCALING

class Level2View(arcade.View):
    def __init__(self):
        super().__init__()

        self.background = None

        self.all_sprites_list = None
        self.all_wall_list = None
        self.static_wall_list = None
        self.moving_wall_list = None
        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.end_of_map = 0
        self.game_over = False

    def setup(self):
        self.background = arcade.load_texture("backgrounds/nature.jpg")

        self.all_wall_list = arcade.SpriteList()
        self.static_wall_list = arcade.SpriteList()
        self.moving_wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("sprite/runner.png", SPRITE_SCALING)
        self.player_sprite.center_x = 2 * GRID_PIXEL_SIZE
        self.player_sprite.center_y = 3 * GRID_PIXEL_SIZE
        self.player_list.append(self.player_sprite)

        for i in range(30):
            wall = arcade.Sprite("sprite/tree.png", SPRITE_SCALING)
            wall.bottom = 0
            wall.center_x = i * GRID_PIXEL_SIZE
            self.static_wall_list.append(wall)
            self.all_wall_list.append(wall)

        wall = arcade.Sprite("sprite/tree.png", SPRITE_SCALING)
        wall.center_y = 3 * GRID_PIXEL_SIZE
        wall.center_x = 3 * GRID_PIXEL_SIZE
        wall.boundary_left = 2 * GRID_PIXEL_SIZE
        wall.boundary_right = 5 * GRID_PIXEL_SIZE
        wall.change_x = 2 * SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)

        wall = arcade.Sprite("sprite/tree.png", SPRITE_SCALING)
        wall.center_y = 3 * GRID_PIXEL_SIZE
        wall.center_x = 7 * GRID_PIXEL_SIZE
        wall.boundary_left = 5 * GRID_PIXEL_SIZE
        wall.boundary_right = 9 * GRID_PIXEL_SIZE
        wall.change_x = -2 * SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)

        wall = arcade.Sprite("sprite/tree.png", SPRITE_SCALING)
        wall.center_y = 5 * GRID_PIXEL_SIZE
        wall.center_x = 5 * GRID_PIXEL_SIZE
        wall.boundary_top = 8 * GRID_PIXEL_SIZE
        wall.boundary_bottom = 4 * GRID_PIXEL_SIZE
        wall.change_y = 2 * SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)

        wall = arcade.Sprite("sprite/tree.png", SPRITE_SCALING)
        wall.center_y = 5 * GRID_PIXEL_SIZE
        wall.center_x = 8 * GRID_PIXEL_SIZE
        wall.boundary_left = 7 * GRID_PIXEL_SIZE
        wall.boundary_right = 9 * GRID_PIXEL_SIZE

        wall.boundary_top = 8 * GRID_PIXEL_SIZE
        wall.boundary_bottom = 4 * GRID_PIXEL_SIZE
        wall.change_x = 2 * SPRITE_SCALING
        wall.change_y = 2 * SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)

        self.physics_engine = \
            arcade.PhysicsEnginePlatformer(self.player_sprite,
                                           self.all_wall_list,
                                           gravity_constant=GRAVITY)
        self.view_left = 0
        self.view_bottom = 0

        self.game_over = False

    def on_draw(self):
        arcade.start_render()

        self.static_wall_list.draw()
        self.moving_wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):

        self.physics_engine.update()

        changed = False
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    level_2_view = Level2View()
    level_2_view.setup()
    window.show_view(level_2_view)
    arcade.run()



if __name__ == "__main__":
    main()