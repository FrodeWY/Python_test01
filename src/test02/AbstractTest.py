from abc import ABCMeta, abstractmethod

import math


class Shape:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.color = 'black'

    @abstractmethod
    def draw(self): pass


class Circle(Shape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def draw(self):
        print('draw circle:(%d, %d, %d)' % (self.x, self.y, self.r))

    def test_pass(self):
        pass

    def move(self, x, y, step, angle=0):
        nx = x + step * math.cos(angle)
        ny = y - step * math.sin(angle)
        return nx, ny


class Line(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y2 = y2
        self.y1 = y1

    def draw(self):
        print('draw line:(%d, %d, %d, %d)' % (self.x1, self.y1, self.x2, self.y2))


def drawCircle(c):
    if isinstance(c, Circle):
        c.draw()


c = Circle(10, 10, 4)
l = Line(0, 0, 5, 5)
list = []
list.append(c)
list.append(l)
for i in range(len(list)):
    cc = list[i]
    if isinstance(cc, (Circle, Line)):
        cc.draw()

drawCircle(c)
c.test_pass()
#  可以同时获得返回值：
x, y = c.move(15, 20, 10, math.pi / 6)
print(x, y)
#  本质Python函数返回的仍然是单一值：返回值是一个tuple
print(c.move(15, 20, 10, math.pi / 6))


def quadratic(a, b, c):

    x1 = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    return x1, x2


x1 ,x2 = quadratic(5, 20, 14)
print(x1,x2)
