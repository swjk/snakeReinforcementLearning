
from environment import Type
import numpy as np
import arcade

class Block():
    @staticmethod
    def draw(lx,rx,top,bottom):
        try:
            arcade.draw_lrtb_rectangle_filled(lx,rx,top,bottom,arcade.color.BLACK)
        except:
            print ("Drawing Error")

class Wall():
    def draw(lx,rx,top,bottom):
        try:
            arcade.draw_lrtb_rectangle_filled(lx,rx,top,bottom,arcade.color.GRAY)
        except:
            print ("Drawing Error")

class SnakeHead(arcade.Sprite):

    def draw(lx,rx,top,bottom):
        try:
            arcade.draw_polygon_filled([[lx,bottom],[rx,bottom], [(lx+rx)/2,top]], arcade.color.RED)
        except:
            print ("Drawing Error")
class SnakeTail():

    def draw(lx,rx,top,bottom):
        arcade.draw_lrtb_rectangle_filled(lx,rx,top,bottom,arcade.color.BLUE)

class Food(arcade.Sprite):

    def draw(lx,rx,top,bottom):
        arcade.draw_lrtb_rectangle_filled(lx,rx,top,bottom,arcade.color.ORANGE)

class Empty():

    def draw(lx,rx,top,bottom):
        arcade.draw_lrtb_rectangle_filled(lx,rx,top,bottom,arcade.color.WHITE)



class Gui(object):
    def __init__(self,screen_width,screen_height,padding,env):
        self.env = env
        self.x_start = padding
        self.x_end   = screen_width - padding
        self.y_start = padding
        self.y_end   = screen_height - padding

    def draw(self):
        env_shape = self.env.env.shape
        x_step = (self.x_end - self.x_start) / env_shape[1]
        y_step = (self.y_end - self.y_start) / env_shape[0]

        for (y,x), value in np.ndenumerate(self.env.env):

            if value == Type.SNAKE_HEAD:

                SnakeHead.draw(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_end-(y_step*y),self.y_end-y_step*(y+1))
            elif value == Type.SNAKE_TAIL:
                SnakeTail.draw(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_end-(y_step*y),self.y_end-y_step*(y+1))
            elif value == Type.FOOD:
                Food.draw(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_end-(y_step*y),self.y_end-y_step*(y+1))

            elif value == Type.BLOCK:
                Block.draw(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_end-(y_step*y),self.y_end-y_step*(y+1))

            elif value == Type.EMPTY:
                Empty.draw(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_end-(y_step*y),self.y_end-y_step*(y+1))

            elif value == Type.WALL:
                Wall.draw(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_end-(y_step*y),self.y_end-y_step*(y+1))
