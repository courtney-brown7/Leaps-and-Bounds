import arcade

PLAYER_MOVEMENT_SPEED = 5

PLAYER_JUMP_SPEED = 25


class LevelView(arcade.View):
    def __init__(self):
        super().__init__()

        self.static_wall_list = None
        self.moving_wall_list = None
        self.background = None
        self.player_list = None
        self.all_sprites_list = None
        self.coin_list = None
        self.all_wall_list = None
        self.player_sprite = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.score = 0
        self.collect_coin_sound = arcade.load_sound("sprite/coin5.wav")
        self.jump_sound = arcade.load_sound("sprite/jump4.wav")

    def on_key_press(self, key, modifiers):
        """When the key is pressed, the character jumps. Takes user input."""
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)

        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """When the user stops holding down a key, the sprite returns to the bottom of the screen."""
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0