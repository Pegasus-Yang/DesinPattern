"""
 @Author: Pegasus-Yang
 @Time: 2021/10/7 10:51
"""
from abc import abstractmethod, ABCMeta


class Shape(metaclass=ABCMeta):
    name = None

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):

    def draw(self):
        self.name = '圆形'
        self.color.paint(self)


class Square(Shape):

    def draw(self):
        self.name = '正方形'
        self.color.paint(self)


class Triangle(Shape):
    def draw(self):
        self.name = '三角形'
        self.color.paint(self)


class Color(metaclass=ABCMeta):
    name = None

    @abstractmethod
    def paint(self, shape):
        pass


class Red(Color):
    def paint(self, shape):
        self.name = '红色'
        print(f'绘制{self.name}的{shape.name}')


class Blue(Color):
    def paint(self, shape):
        self.name = '蓝色'
        print(f'绘制{self.name}的{shape.name}')


class Green(Color):
    def paint(self, shape):
        self.name = '绿色'
        print(f'绘制{self.name}的{shape.name}')


if __name__ == '__main__':
    Triangle(Red()).draw()
    Circle(Blue()).draw()
    Square(Green()).draw()
