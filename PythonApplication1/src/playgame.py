SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "SNAKE"
PADDING = 200

from level import level1
import environment
import snake
import arcade
import gui

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

        self.env = environment.Environment(level1)
        print(self.env)
        self.gui = gui.Gui(SCREEN_WIDTH,SCREEN_HEIGHT,PADDING,self.env)


    def on_draw(self):
        arcade.start_render()
        #arcade.draw_lrtb_rectangle_filled(20,200,200,100, arcade.color.WISTERIA)
        #arcade.draw_circle_outline(300, 285, 18, arcade.color.WISTERIA, 3)
        self.gui.draw()
        arcade.finish_render()




    def on_key_press(self,symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT or symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            pass

    def update(self,x):
        pass




def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()
