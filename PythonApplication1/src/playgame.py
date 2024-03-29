SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "SNAKE"
PADDING = 250



from level import level1
import environment
import snake
import arcade
import gui
from util import FPSCounter
from dql import Dql
from PIL import Image
from gamestate import GameState,SnakeEnvState,Reward

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

        self.env = environment.Environment(level1)
        self.gui = gui.Gui(SCREEN_WIDTH,SCREEN_HEIGHT,PADDING,self.env)
        self.set_update_rate(1/60)
        self.fps = FPSCounter()
        self.gamestate = GameState.GAME_RUNNING
        self.timer = 0

    def initial_display_state(self):
        arcade.start_render()
        self.gui.draw(self.gamestate)
        arcade.finish_render()


    def on_draw(self):
        fps = self.fps.get_fps()

        self.fps.tick()

        arcade.start_render()
        self.gui.draw(self.gamestate)
        arcade.finish_render()

    def on_key_press(self,symbol, modifiers):
        self.env.change_snake_dir(symbol)

    def on_update(self,x):
        if(self.gamestate == GameState.GAME_OVER):
            pass
        elif(self.gamestate == GameState.GAME_RUNNING):
            snake_env_state =  self.env.update()
            self.gui.update()
            if snake_env_state == SnakeEnvState.EATEN:
                return Reward.POS
            elif snake_env_state == SnakeEnvState.COLLISION:
                self.gamestate = GameState.GAME_OVER
                return Reward.NEG
            else:
                return Reward.NORM


            # if self.timer + x > 1/10:
            #     self.timer = 0
            #     update_result = self.env.update()
            #     self.gui.update()
            #     if update_result:
            #         self.gamestate = GameState.GAME_OVER
            #
            # else:
            #     self.timer += x




def main():
    window = GameWindow()
    #window.initial_display_state()
    #arcade.get_image()
    arcade.run()

if __name__ == "__main__":
    main()
