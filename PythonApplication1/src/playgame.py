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

        self.gui = gui.Gui(SCREEN_WIDTH,SCREEN_HEIGHT,PADDING,self.env)


    def on_draw(self):
        arcade.start_render()
        self.gui.draw()




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
