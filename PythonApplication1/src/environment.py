
import numpy as np
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


    def createGrid(self,load_level):
        self._cells = np.array([[self._cell_type_map[char] for char in line]
            for line in load_level])
