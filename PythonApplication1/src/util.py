
import math

class Vector(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getTuple(self):
        return self.x,self.y


class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getTuple(self):
        return self.x,self.y

    def addVector(self, vector):
        v1,v2 = vector.getTuple()
        self.x = self.x + v1
        self.y = self.y + v2

    def distance(self, other):
        x2,y2 = other.getTuple()
        return math.hypot(self.x - x2, self.y-y2)

    def __str__(self):
        return "Point({},{})".format(self.x,self.y)

    def __repr__(self):
        return str(self)
