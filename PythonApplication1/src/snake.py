from collections import deque
from util import Vector,Point


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
        self.extend = false


    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def move(self):
        if not self.extend:
            self.tail.pop()
        self.tail.appendleft(self.head)
        self.head = (self.head).addVector(self.direction)
