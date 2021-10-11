"""
 @Author: Pegasus-Yang
 @Time: 2021/10/7 11:35
"""
from abc import abstractmethod, ABCMeta


class Graphic(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        pass


class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(self)

    def __str__(self):
        return f'[{self.x},{self.y}]'


class Line(Graphic):

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self):
        print(self)

    def __str__(self):
        return f'line:{self.point_a}-{self.point_b}'


class Circle(Graphic):
    def __init__(self, center_point, radius):
        self.center_point = center_point
        self.radius = radius

    def draw(self):
        print(self)

    def __str__(self):
        return f'circle:center_point:{self.center_point},radius:{self.radius}'


class Square(Graphic):

    def __init__(self, line_n, line_s, line_w, line_e):
        self.line_n = line_n
        self.line_s = line_s
        self.line_w = line_w
        self.line_e = line_e

    def draw(self):
        print(self)

    def __str__(self):
        return f'square:north:{self.line_n},south：{self.line_s},west:{self.line_w},east:{self.line_e}'


class Complex(Graphic):

    def __init__(self, child=None):
        self.child = []
        if child:
            for i in child:
                self.child.append(i)

    def draw(self):
        print('#' * 20 + 'Complex' + '#' * 20)
        for i in self.child:
            i.draw()
        print('#' * 20 + 'Complex' + '#' * 20)

    def add(self, child):
        self.child.append(child)


if __name__ == '__main__':
    p1 = Point(3, 5)
    p1.draw()
    l1 = Line(Point(1, 2), Point(4, 5))
    l1.draw()
    c1 = Circle(Point(1, 2), 15)
    c1.draw()
    c2 = Circle(Point(5, 5), 3)
    c2.draw()
    s1 = Square(Line(Point(0, 3), Point(3, 3)), Line(Point(0, 0), Point(3, 0)), Line(Point(0, 0), Point(0, 3)),
                Line(Point(3, 0), Point(3, 3)))
    s1.draw()
    co1 = Complex([l1, s1, c2])
    co1.draw()
    co1.add(c1)
    co1.draw()

