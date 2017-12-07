from abc import ABCMeta,abstractmethod


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
    if isinstance(cc, Shape):
        cc.draw()

drawCircle(c)
