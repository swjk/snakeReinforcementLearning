
from environment import Type
import numpy as np
import arcade
from snake import Direction
from gamestate import GameState
from PIL import Image

class Block(arcade.Sprite):
    def __init__(self,lx,rx,top, bottom):
        super().__init__("./small.png")
        self.center_x = (lx+rx)/2
        self.center_y = (top+bottom)/2

        self.height = abs(top-bottom)
        self.width = abs(lx-rx)
        self._set_color(arcade.color.BLACK)

class Wall(arcade.Sprite):
    def __init__(self,lx,rx,top, bottom):
        super().__init__("./small.png")
        self.center_x = (lx+rx)/2
        self.center_y = (top+bottom)/2

        self.height = abs(top-bottom)
        self.width = abs(lx-rx)
        self._set_color(arcade.color.BLACK)

class SnakeHead(arcade.Sprite):
    def __init__(self,lx,rx,top, bottom):
        super().__init__("./small.png")

        self.center_x = (lx+rx)/2
        self.center_y = (top+bottom)/2
        self.height = abs(top-bottom)
        self.width = abs(lx-rx)

        self._set_color(arcade.color.BLIZZARD_BLUE)

class SnakeTail(arcade.Sprite):
    def __init__(self,lx=None,rx=None,top=None, bottom=None, center_x=None, center_y=None, height=None, width=None):
        super().__init__("./small.png")
        self._set_color(arcade.color.DAFFODIL)
        if center_x == None:
            self.center_x = (lx+rx)/2
            self.width = abs(lx-rx)
        else:
            self.center_x = center_x
            self.width = width
        if center_y == None:
            self.center_y = (top+bottom)/2
            self.height = abs(top-bottom)
        else:
            self.center_y = center_y
            self.height = height




class Food(arcade.Sprite):
    def __init__(self,lx,rx,top, bottom):
        super().__init__("./small.png")

        self.center_x = (lx+rx)/2
        self.center_y = (top+bottom)/2
        self.height = abs(top-bottom)
        self.width = abs(lx-rx)

        self._set_color(arcade.color.ORANGE)

class Empty(arcade.Sprite):
    def __init__(self,lx,rx,top, bottom):
        super().__init__("./small.png")

        self.center_x = (lx+rx)/2
        self.center_y = (top+bottom)/2
        self.height = abs(top-bottom)
        self.width = abs(lx-rx)

        self._set_color(arcade.color.WHITE)


class Gui(object):
    def __init__(self,screen_width,screen_height,padding,env):
        self.env = env
        print(env)
        self.x_start = padding
        self.x_end   = screen_width - padding
        self.y_start = padding
        self.y_end   = screen_height - padding

        print (self.x_end)
        print (self.x_start)

        self.grid_sprite = arcade.SpriteList()
        self.snake_sprite = arcade.SpriteList()
        self.snake_head = None
        self.food_sprite = arcade.SpriteList()

        self.initial_sprite_setup()

    def initial_sprite_setup(self):
        env_shape = self.env.env.shape
        x_step = (self.x_end - self.x_start) / env_shape[1]
        y_step = (self.y_end - self.y_start) / env_shape[0]
        for (y,x), value in np.ndenumerate(self.env.grid._cells):
            if value == Type.BLOCK:
                self.grid_sprite.append(Block(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_end-(y_step*y),self.y_end-y_step*(y+1)))
            elif value == Type.EMPTY:
                self.grid_sprite.append(Empty(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_end-(y_step*y),self.y_end-y_step*(y+1)))
            elif value == Type.WALL:
                self.grid_sprite.append(Wall(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_end-(y_step*y),self.y_end-y_step*(y+1)))

        x,y = self.env.snake.get_head().getTuple()
        self.snake_head = SnakeHead(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_end-(y_step*y),self.y_end-y_step*(y+1))

        self.snake_sprite.append(self.snake_head)

        for tail_point in self.env.snake.get_tail():
            x,y = tail_point.getTuple()
            self.snake_sprite.append(SnakeTail(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_end-(y_step*y),self.y_end-y_step*(y+1)))

        x,y = self.env.food.get_food().getTuple()
        self.food_sprite.append(Food(self.x_start + x_step*x, self.x_start + x_step*(x+1),self.y_end-(y_step*y),self.y_end-y_step*(y+1)))

    def draw_game_over(self):

        output = "Game Over"
        arcade.draw_text(output, 100, 100, arcade.color.WHITE, 54)



    def draw(self, gamestate):
        if gamestate == GameState.GAME_RUNNING:
            self.grid_sprite.draw()
            self.snake_sprite.draw()
            self.food_sprite.draw()
        else:
            self.draw_game_over()


    def update(self):

        env_shape = self.env.env.shape
        x_step = (self.x_end - self.x_start) / env_shape[1]
        y_step = (self.y_end - self.y_start) / env_shape[0]

        x,y = self.env.snake.get_head().getTuple()

        if self.env.food.relocated:
            for food_sprite in self.food_sprite.sprite_list:
                x_food,y_food =  self.env.food.get_food().getTuple()
                center_x = (self.x_start + x_step*(x_food+1) + self.x_start + x_step*x_food) / 2
                center_y = ((self.y_end-(y_step*y_food)) + (self.y_end-y_step*(y_food+1))) / 2
                food_sprite.set_position(center_x, center_y)

        last_sprite_center_x, last_sprite_center_y = self.snake_sprite.sprite_list[-1].center_x,self.snake_sprite.sprite_list[-1].center_y

        for idx, sprite in reversed(list(enumerate(self.snake_sprite.sprite_list))):
            if idx > 0:
                print (idx)
                sprite.set_position(self.snake_sprite.sprite_list[idx-1].center_x,self.snake_sprite.sprite_list[idx-1].center_y)

        if self.env.snake.extend:
             self.snake_sprite.append(SnakeTail(center_x=last_sprite_center_x, center_y=last_sprite_center_y, height=y_step, width=x_step))

        center_x = (self.x_start + x_step*(x+1) + self.x_start + x_step*x) / 2
        center_y = ((self.y_end-(y_step*y)) + (self.y_end-y_step*(y+1))) / 2
        self.snake_head.set_position(center_x, center_y)
