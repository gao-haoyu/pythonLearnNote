## python学习--day11
**内容概述**
- class进阶
****
重点知识
- 类的继承基本概念
- overriding
- 抽象基类
- 多态
****

### 类的继承基本概念
```text
基本形式：
    class SubClass(BaseClass):
        ...  
基本特点：
    子类继承基类的成员变量&成员函数
```
```python
# 示例代码
class Base:
    def __init__(self):
        self.val = 1

    def action1(self):
        print('action1')


class Sub(Base):
    def action2(self):
        print('action2')


b = Sub()
print(b.val)             # 1
b.action1()              # action1
b.action2()              # action2
```
### 继承中的overriding
```text
overriding的定义：
    子类中覆写父类中的函数，从而实现不同类型的对象调用同一个函数名出现不同的结果(多态)
```
```python
class Base:
    def __init__(self):
        self.val = 1

    def test(self):
        print('test Base class')

class Sub(Base):
    def __init__(self):
        self.val = 2

    def test(self):
        print('test Sub class')


a = Base()
b = Sub()
print(a.val, b.val)        # 1 2
a.test()                   # test Base class
b.test()                   # test Sub class
```
```python
# 一个引申问题：当被覆写的函数中依然想拥有基类的函数功能是，采用super()函数来获取。见示例代码
class Base:
    def __init__(self):
        self.Baseval = 1


class Sub(Base):
    def __init__(self):
        super().__init__()
        self.Subval = 2


b = Sub()
print(b.Baseval, b.Subval)   # 1 2
```
### 多重继承
```text
基本形式：
    class Sub(Base1, Base2):
        ...
作用：
    拥有多个类的属性
```
```python
class Flyer:
    def fly(self):
        pass
    
    
class Swimmer:
    def swim(self):
        pass
    
    
class FlyFish(Flyer, Swimmer):        # 同时具有fly和swim的属性
    pass
```
```python
# 一个多重继承的反面案例
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


ff1 = FlyFish1()
ff1.eat()                # flyer eating
ff2 = FlyFish2()
ff2.eat()                # swimmer eating
```
```text
问题分析：
    可以看到FlyFish1和FlyFish2之间因为继承顺序不同，导致调用同名函数时，结果不一样，这是很糟糕。
    不符合常规逻辑，在设计时，要避免这种情况。
```
**一个继承的好的例子**
```python
class InvalidOperator(Exception):  # 自定义异常类型
    pass


class Stream:
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


class FileStream(Stream):
    def read(self):
        print('Read data from file stream')


class NetworkStream(Stream):
    def read(self):
        print('Read data from network stream')
```

**关于继承的tips**
```text
    1. 尽量避免复杂的多级继承，限制继承层数在1-2之间
    2. 多重继承的使用，要仔细，应保证多个父类之间没有交集
```

### 抽象基类
```text
实现手段：
    1.引入ABC基类
    2.调用abstractmethod装饰器来修饰纯虚函数
实现目的：
    1.避免抽象基类被实例化，引发不可预期的后果
    2.设置纯虚函数，强制子类进行overriding
```
```python
# task：将上面的stream改写成抽象基类
from abc import ABC, abstractmethod
class InvalidOperator(Exception):  # 自定义异常类型
    pass

class Stream(ABC):                   #引入ABC基类
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

    @abstractmethod                #引入abstractmethod
    def read(self):
        pass
```

### 多态的实现
```text
定义：
    不同的对象，调用同一个函数，不同的效果。
    灵活运用，可以增加程序的灵活性。
```
```python
from abc import ABC, abstractmethod


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
'''
Draw TextBox
Draw DropDownList
'''
```
```text
一点分析;
    在python并不一定是严格的继承关系，才能实现多态的形式。
    事实上，多态运行时只去检查传入的对象是否具有需要调用的方法。
    是否具有逻辑上的类的关联，是设计人员自己更为关心的，是为了庞大程序拥有更为清晰的代码逻辑。
```

### 关于类的一点补充
```text
    1.内置的类也可继承&覆写
    2.纯数据类，可以采用一种新颖的方法 namedtuple
```
```python
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
 
'''
True
True
'''
#可以看到，两者达到了同样的效果。namedtuple适用与简单的数据类，不包含复杂的运算&赋值操作
```