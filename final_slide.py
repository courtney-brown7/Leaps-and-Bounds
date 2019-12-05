import arcade

SCREEN_HEIGHT = 650
SCREEN_WIDTH = 1000




class FinalView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("CONGRATS YOU'VE WON!!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("TOTAL SCORE:", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Different Views Example")
    final_view = FinalView()
    window.show_view(final_view)
    arcade.run()


if __name__ == "__main__":
    main()
