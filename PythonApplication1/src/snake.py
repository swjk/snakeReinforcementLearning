from collections import deque
from util import Vector,Point
import copy

class Direction(object):
    UP    = Vector(0,-1)
    DOWN  = Vector(0,1)
    LEFT  = Vector(-1,0)
    RIGHT = Vector(1,0)

class Snake(object):
    def __init__(self,head,tail):
        self.head   = head
        self.direction = Direction.UP
        self.velocity  = 1
        self.tail = deque(tail)
        self.extend = False
        self.snake_directions = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def turn_left(self):
        current_dir_index = self.snake_directions.index(self.direction)
        self.direction = self.snake_directions[(current_dir_index - 1) % len(self.snake_directions)]

    def turn_right(self):
        current_dir_index = self.snake_directions.index(self.direction)
        self.direction = self.snake_directions[(current_dir_index+1) % len(self.snake_directions)]

    def extend_tail(self):
        self.extend = True

    def update(self):
        self.move()
        self.extend = False

    def move(self):
        if not self.extend:
            self.tail.pop()
        self.tail.appendleft(copy.copy(self.head))
        self.head.addVector(self.direction)
