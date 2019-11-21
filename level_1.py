import arcade

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 400
SCREEN_TITLE = 'Endless Stairs'
CHARACTER_SCALING = .05

class GameWindow(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.background = None

    def setup(self):
        self.background = arcade.load_texture("backgrounds/beach.png")
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("sprite/chicken.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 120
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player_list.draw()


'''class Sprite(arcade.Sprite):
    def __init__ (self): 
        self.player_list = None
    def setup(self):
        
       
       

    def on_draw(self):
        arcade.start_render()

        self.wall_list.draw()
        self.coin_list.draw()

'''

def main():
    """ Main method """
    window = GameWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
