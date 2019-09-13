
import numpy as np
from util import Point
import snake

class Type(object):
    SNAKE_HEAD = 0
    SNAKE_TAIL = 1
    WALL = 2
    FOOD = 3
    BLOCK = 4
    EMPTY = 5


class Environment(object):

    def __init__(self, level):
        grid = Grid()
        self.env   = np.copy(grid.load_level(level))
        self.snake = snake.Snake(grid.find_init_snake_head(),grid.find_init_snake_tail())
        self.food  = Food(grid.find_init_food())
        self.grid  = grid.create_grid()

    def __str__(self):
        return np.array_str(self.env)



    def updateEnv(self):
        pass




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
    def __init__(self,pos):
        self.pos = pos



    def random_relocate():
        pass
