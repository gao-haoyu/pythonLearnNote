# 继承
class Base:
    def __init__(self):
        self.Baseval = 1


class Sub(Base):
    def __init__(self):
        super().__init__()
        self.Subval = 2


# b = Sub()
# print(b.Baseval, b.Subval)


class Flyer:
    def fly(self):
        pass

    def eat(self):
        print('flyer eating')


class Swimmer:
    def swim(self):
        pass

    def eat(self):
        print('swimmer eating')


class FlyFish1(Flyer, Swimmer):
    pass


class FlyFish2(Swimmer, Flyer):
    pass

'''
ff1 = FlyFish1()
ff1.eat()
ff2 = FlyFish2()
ff2.eat()
'''


class InvalidOperator(Exception):  # 自定义异常类型
    pass


from abc import ABC, abstractmethod


class Stream(ABC):
    def __init__(self):
        self.openstatus = False

    def open(self):
        if self.openstatus:
            raise InvalidOperator('Data has been opened.')
        self.openstatus = True

    def close(self):
        if not self.openstatus:
            raise InvalidOperator('Data has been closed')
        self.openstatus = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print('Read data from file stream')


class NetworkStream(Stream):
    def read(self):
        print('Read data from network stream')


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Draw TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("Draw DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


textbox = TextBox()
dropdownlist = DropDownList()
lst= [textbox, dropdownlist]
draw(lst)


class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


from collections import namedtuple
Point2 = namedtuple("Point2", ['x', 'y'])

p11 = Point1(1, 2)
p12 = Point1(1, 2)
print(p11 == p12)
p21 = Point2(3, 4)
p22 = Point2(3, 4)
print(p21 == p22)
