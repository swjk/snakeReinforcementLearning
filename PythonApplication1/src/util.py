
import math
import time
import collections

class Vector(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "Vector({},{})".format(self.x, self.y)

    def getTuple(self):
        return (self.x,self.y)

class FPSCounter:
    def __init__(self):
        self.time = time.perf_counter()
        self.frame_times = collections.deque(maxlen=60)

    def tick(self):
        t1 = time.perf_counter()
        dt = t1 - self.time
        self.time = t1
        self.frame_times.append(dt)

    def get_fps(self):
        total_time = sum(self.frame_times)
        if total_time == 0:
            return 0
        else:
            return len(self.frame_times) / sum(self.frame_times)



class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __copy__(self):
        return Point(self.x,self.y)

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

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
