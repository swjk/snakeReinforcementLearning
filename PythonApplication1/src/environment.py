
import numpy as np
from util import Point
import snake
import arcade
import random
from dql import AgentActions
from gamestate import SnakeEnvState


class Type(object):
    SNAKE_HEAD = 0
    SNAKE_TAIL = 1
    WALL = 2
    FOOD = 3
    BLOCK = 4
    EMPTY = 5


class Environment(object):

    def __init__(self, level):
        self.grid = Grid()
        self.env   = np.copy(self.grid.load_level(level))
        self.snake = snake.Snake(self.grid.find_init_snake_head(),self.grid.find_init_snake_tail())
        self.food  = Food(self.grid.find_init_food(), self.grid.get_cell_shape())
        self.grid.create_grid()
        self.counter = 0

    def __str__(self):
        return np.array_str(self.env)

    def place_snake(self,env):
        snake_head = self.snake.get_head()
        snake_tail = self.snake.get_tail()

        env[snake_head.getTuple()[1], snake_head.getTuple()[0]] = Type.SNAKE_HEAD
        for tail_point in snake_tail:
            env[tail_point.getTuple()[1], tail_point.getTuple()[0]] = Type.SNAKE_TAIL

    def place_food(self,env):
        food_point = self.food.get_food()
        env[food_point.getTuple()[1], food_point.getTuple()[0]] = Type.FOOD


    def change_snake_dir(self, symbol):
        if symbol == arcade.key.LEFT or symbol == AgentActions.LEFT:
            self.snake.turn_left()

        elif symbol == arcade.key.RIGHT or symbol == AgentActions.RIGHT:
            self.snake.turn_right()
        elif symbol == AgentActions.NO_ACTION:
            pass

    def update_env(self):
        self.snake.update()
        self.food.update()
        self.env = np.copy(self.grid.get_cells())
        self.place_food(self.env)
        self.place_snake(self.env)

    def check_collisions(self):
        head_point = self.snake.get_head()
        head_x,head_y = head_point.getTuple()

        if head_point in self.snake.get_tail():
            return SnakeEnvState.COLLISION
        elif head_point == self.food.get_food():
            self.snake.extend_tail()
            self.food.random_relocate(self.env)
            return SnakeEnvState.EATEN
        elif self.grid.get_cells()[head_y][head_x] in (Type.BLOCK, Type.WALL):
            return SnakeEnvState.COLLISION

        return SnakeEnvState.NORM

    def update(self):
        self.update_env()
        return self.check_collisions()



class Grid(object):

    def __init__(self):
        self._cell_type_env = {
            'S': Type.SNAKE_HEAD,
            'T': Type.SNAKE_TAIL,
            'W': Type.WALL,
            'F': Type.FOOD,
            'B': Type.BLOCK,
            'E': Type.EMPTY
        }
        self._cell_type_grid = {

        }
        self._cells = None

    def __getitem__(self,point):
        x,y = point
        return self._cells[y,x]


    def __setitem__(self,point,type):
        x,y = point
        self._cells[y,x] = type

    def get_cells(self):
        return self._cells

    def get_cell_shape(self):
        return self._cells.shape

    def load_level(self, level):
        self._cells = np.array([[self._cell_type_env[char] for char in line]
            for line in level])
        return self._cells

    def create_grid(self):
        for (y,x),value in np.ndenumerate(self._cells):
            if value == Type.FOOD or value == Type.SNAKE_HEAD or value == Type.SNAKE_TAIL:
                self._cells[y,x] = Type.EMPTY

    def find_init_snake_head(self):
        for (y,x),value in np.ndenumerate(self._cells):
            if value == Type.SNAKE_HEAD:
                return Point(x,y)

    def find_init_snake_tail(self):
        head = self.find_init_snake_head()
        tail = []
        for (y,x),value in np.ndenumerate(self._cells):
            if value == Type.SNAKE_TAIL:
                tail.append(Point(x,y))


        tail.sort(key=lambda point: head.distance(point))
        return tail

    def find_init_food(self):
        for (y,x), value in np.ndenumerate(self._cells):
            if value == Type.FOOD:
                return Point(x,y)



class Food(object):
    def __init__(self,pos,grid_shape):
        self.pos = pos
        self.grid_shape = grid_shape
        self.relocated = False

    def get_food(self):
        return self.pos

    def update(self):
        self.relocate = False

    def random_relocate(self, env):
        print (self.grid_shape)
        y = random.randint(0,self.grid_shape[0]-1)
        x = random.randint(0,self.grid_shape[1]-1)
        while env[y,x] != Type.EMPTY:
            y = random.randint(0,self.grid_shape[0]-1)
            x = random.randint(0,self.grid_shape[1]-1)
            print (y)
        self.pos = Point(x,y)
        self.relocated = True
