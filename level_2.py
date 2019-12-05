import arcade

from Level import LevelView

CHARACTER_SCALING = 0.2
SPRITE_SCALING = 0.1
SCREEN_HEIGHT = 650
SCREEN_WIDTH = 1000
SCREEN_TITLE = 'Mountain Level'
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = 30

VIEWPORT_MARGIN = SPRITE_PIXEL_SIZE * SPRITE_SCALING
RIGHT_MARGIN = 4 * SPRITE_PIXEL_SIZE * SPRITE_SCALING

MOVEMENT_SPEED = 10
JUMP_SPEED = 15
GRAVITY = 1


class Level2View(LevelView):

    def __init__(self):
        super().__init__()

    def on_show(self):
        self.background = arcade.load_texture("backgrounds/nature.jpg")

    def setup(self):

        self.all_wall_list = arcade.SpriteList()
        self.static_wall_list = arcade.SpriteList()
        self.moving_wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # sprite setup
        self.player_sprite = arcade.Sprite("sprite/jumping_char.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 2 * GRID_PIXEL_SIZE
        self.player_sprite.center_y = 3 * GRID_PIXEL_SIZE
        self.player_list.append(self.player_sprite)

        # bush floor
        for i in range(40):
            wall = arcade.Sprite("sprite/hills.png", SPRITE_SCALING)
            wall.bottom = 0
            wall.center_x = i * GRID_PIXEL_SIZE
            self.static_wall_list.append(wall)
            self.all_wall_list.append(wall)

        self.make_platform(3, 6, 4, 9, 7)
        self.make_platform(5, 7, 10, 15, 6)
        self.make_platform(7, 9, 17, 20, 10)
        self.make_platform(4, 16, 23, 26, 0, 4, 4, 7)
        self.make_platform(30, 7, 17, 20, 4)

        self.physics_engine = \
            arcade.PhysicsEnginePlatformer(self.player_sprite,
                                           self.all_wall_list,
                                           gravity_constant=GRAVITY)
        self.view_left = 0
        self.view_bottom = 0

    def make_platform(self, center_y, center_x, boundary_left, boundary_right, change_x, boundary_top=0,
                      boundary_bottom=0, change_y=0):

        wall = arcade.Sprite("sprite/hills.png", SPRITE_SCALING)
        wall.center_y = center_y * GRID_PIXEL_SIZE
        wall.center_x = center_x * GRID_PIXEL_SIZE
        wall.boundary_left = boundary_left * GRID_PIXEL_SIZE
        wall.boundary_right = boundary_right * GRID_PIXEL_SIZE
        wall.change_x = change_x * SPRITE_SCALING

        if wall.boundary_top is not None:
            wall.boundary_top = boundary_top * GRID_PIXEL_SIZE
        if wall.boundary_bottom is not None:
            wall.boundary_bottom = boundary_bottom * GRID_PIXEL_SIZE
        if wall.change_y is not None:
            wall.change_y = change_y * SPRITE_SCALING
        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
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

        ''' if self.score == 4:
            self.window.show_view(level_3.main())
        '''


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    level_2_view = Level2View()
    level_2_view.setup()
    window.show_view(level_2_view)
    arcade.run()


if __name__ == "__main__":
    main()
