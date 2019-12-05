import arcade
import level_1


SCREEN_HEIGHT = 650
SCREEN_WIDTH = 1000


class IntroView(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.BLUE_BELL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("LEVEL UP!!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to PLAY!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        first_level = level_1.Level1View()
        first_level.setup()
        self.window.show_view(first_level)


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Different Views Example")
    window.total_score = 0
    intro_view = IntroView()
    window.show_view(intro_view)
    arcade.run()


if __name__ == "__main__":
    main()
