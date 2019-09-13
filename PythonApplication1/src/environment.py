
import numpy as np
from util import Point

class Type(object):
    SNAKE_HEAD = 0
    SNAKE_TAIL = 1
    WALL = 2
    FOOD = 3
    BLOCK = 4
    EMPTY = 5

class Grid(object):

    def __init__(self):
        self._cell_type_map = {
            'S': Type.SNAKE_HEAD,
            'T': Type.SNAKE_TAIL,
            'W': Type.WALL,
            'F': Type.FOOD,
            'B': Type.BLOCK,
            'E': Type.EMPTY
        }
        self._cells = None

    def __getitem__(self,point):
        x,y = point
        return self._cells[y,x]


    def __setitem__(self,point,type):
        x,y = point
        self._cells[y,x] = type


    def create_grid(self,load_level):
        self._cells = np.array([[self._cell_type_map[char] for char in line]
            for line in load_level])

    def find_snake_head(self):
        for (y,x),value in np.ndenumerate(self._cells):
            if value == Type.SNAKE_HEAD:
                return Point(x,y)

    def find_snake_tail(self):
        head = self.find_snake_head()
        tail = []
        for (y,x),value in np.ndenumerate(self._cells):
            if value == Type.SNAKE_TAIL:
                tail.append(Point(x,y))
        

        tail.sort(key=lambda point: head.distance(point))
        return tail


class Fruit(object):
    def __init__(self,pos):
        self.pos = pos

    def random_relocate():
        pass
