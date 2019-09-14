
from environment import Type
import numpy as np
import arcade
from snake import Direction

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
        self._set_color(arcade.color.RED)

class SnakeHead(arcade.Sprite):
    def __init__(self,lx,rx,top, bottom):
        super().__init__("./small.png")

        self.center_x = (lx+rx)/2
        self.center_y = (top+bottom)/2
        self.height = abs(top-bottom)
        self.width = abs(lx-rx)

        self._set_color(arcade.color.BLUE)

    # @staticmethod
    # def draw(lx,rx,top,bottom, direction):

        # try:
        #     if direction == Direction.UP:
        #         arcade.draw_polygon_filled([[lx,bottom],[rx,bottom], [(lx+rx)/2,top]], arcade.color.RED)
        #     elif direction == Direction.DOWN:
        #         arcade.draw_polygon_filled([[lx,top],[rx,top], [(lx+rx)/2,bottom]], arcade.color.RED)
        #     elif direction == Direction.LEFT:
        #         arcade.draw_polygon_filled([[rx,top],[rx,bottom], [(lx),(top+bottom)/2]], arcade.color.RED)
        #     elif direction == Direction.RIGHT:
        #         arcade.draw_polygon_filled([[lx,top],[lx,bottom], [(rx),(top+bottom)/2]], arcade.color.RED)
        # except:
        #     print ("Drawing Error")
class SnakeTail(arcade.Sprite):
    def __init__(self,lx,rx,top, bottom):
        super().__init__("./small.png")

        self.center_x = (lx+rx)/2
        self.center_y = (top+bottom)/2
        self.height = abs(top-bottom)
        self.width = abs(lx-rx)

        self._set_color(arcade.color.RED)
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

    def draw(self):
        self.grid_sprite.draw()
        self.snake_sprite.draw()
        self.food_sprite.draw()


    def update(self):

        env_shape = self.env.env.shape
        x_step = (self.x_end - self.x_start) / env_shape[1]
        y_step = (self.y_end - self.y_start) / env_shape[0]

        x,y = self.env.snake.get_head().getTuple()

        for idx, sprite in reversed(list(enumerate(self.snake_sprite.sprite_list))):

            if idx > 0:
                print (idx)
                sprite.set_position(self.snake_sprite.sprite_list[idx-1].center_x,self.snake_sprite.sprite_list[idx-1].center_y)


        center_x = (self.x_start + x_step*(x+1) + self.x_start + x_step*x) / 2
        center_y = ((self.y_end-(y_step*y)) + (self.y_end-y_step*(y+1))) / 2
        self.snake_head.set_position(center_x, center_y)
