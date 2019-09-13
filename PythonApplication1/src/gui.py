
from environment import Type
import numpy as np
import arcade

class Block(arcade.Sprite):
    def __init__(self,lx,rx,top,bottom):
        self.lx = lx
        self.rx = rx
        self.top = top
        self.bottom = bottom

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(self.lx,self.rx,self.top,self.bottom,arcade.color.BLACK)


class Wall(arcade.Sprite):
    def __init__(self,lx,rx,top,bottom):
        self.lx = lx
        self.rx = rx
        self.top = top
        self.bottom = bottom

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(self.lx,self.rx,self.top,self.bottom,arcade.color.GRAY)


class SnakeHead(arcade.Sprite):
    def __init__(self,lx,rx,top,bottom):
        self.lx = lx
        self.rx = rx
        self.top = top
        self.bottom = bottom

    def draw(self):
        arcade.draw_polygon_filled([[lx,bottom],[rx,bottom], [(lx+rx)/2,top]], arcade.color.RED)

class SnakeTail(arcade.Sprite):
    def __init__(self,lx,rx,top,bottom):
        self.lx = lx
        self.rx = rx
        self.top = top
        self.bottom = bottom

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(self.lx,self.rx,self.top,self.bottom,arcade.color.BLUE)

class Food(arcade.Sprite):
    def __init__(self,lx,rx,top,bottom):
        self.lx = lx
        self.rx = rx
        self.top = top
        self.bottom = bottom

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(self.lx,self.rx,self.top,self.bottom,arcade.color.ORANGE)

class Empty(arcade.Sprite):
    def __init__(self,lx,rx,top,bottom):
        self.lx = lx
        self.rx = rx
        self.top = top
        self.bottom = bottom

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(self.lx,self.rx,self.top,self.bottom,arcade.color.WHITE)


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
                SnakeHead(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_start+y_step*y,self.y_start+y_step*(y+1)).draw()
            elif value == Type.SNAKE_TAIL:
                SnakeTail(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_start+y_step*y,self.y_start+y_step*(y+1)).draw()
            elif value == Type.FOOD:
                Food(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_start+y_step*y,self.y_start+y_step*(y+1)).draw()
            elif value == Type.BLOCK:
                Block(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_start+y_step*y,self.y_start+y_step*(y+1)).draw()
            elif value == Type.EMPTY:
                Empty(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_start+y_step*y,self.y_start+y_step*(y+1)).draw()
            elif value == Type.WALL:
                Wall(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_start+y_step*y,self.y_start+y_step*(y+1)).draw()
