## python学习--day12
**内容概述**
- 模组(modules)
****
重点知识
- modules的基本概念
****

### modules的基本概念
```text
基本形式：
    将文件分包，通过调用的方式得到其它文件所定义的功能
基本作用：
    让代码更加清晰
```
```python
# 不采用模组代码示例
from abc import ABC, abstractmethod


class Fruit(ABC):
    def __init__(self):
        self.weight = 0
        self.price = 0

    @abstractmethod
    def set_price(self, value):
        pass

    def get_price(self):
        return self.price


class Apple(Fruit):
    def set_price(self, value):
        self.price = value


class Banana(Fruit):
    def set_price(self, value):
        self.price = value


a = Apple()
a.set_price(10)
print(a.get_price())

b = Banana()
b.set_price(20)
print(b.price)
```
```python
# 利用modules将文件拆分
# fruits.py
from abc import ABC, abstractmethod


class Fruit(ABC):
    def __init__(self):
        self.weight = 0
        self.price = 0

    @abstractmethod
    def set_price(self, value):
        pass

    def get_price(self):
        return self.price


class Apple(Fruit):
    def set_price(self, value):
        self.price = value


class Banana(Fruit):
    def set_price(self, value):
        self.price = value

# main.py  第一种调用方式
from fruits import Apple, Banana     #若为了简化代码可以 from fruits import *  但不够清晰，一般不建议


a = Apple()
a.set_price(10)
print(a.get_price())

b = Banana()
b.set_price(20)
print(b.price)
```
```python
# main.py 第二种调用方式
import fruits             # 将整个文件作为一个类模块

a = fruits.Apple()        # 具体代码调用时，要包含fruits这一头
a.set_price(10)
print(a.get_price())

b = fruits.Banana()
b.set_price(20)
print(b.price)
```

### 设置package路径
```text
    一般而言，pycharm在发现引用文件更改位置之后，会自动更新位置。
    当将引用的文件放置在一个新的文件夹下，新的文件中设计一个__init__.py的空文件，之后便可正常引入该文件夹中的文件
    其形式为：
    from package import fruits

    a = fruits.Apple() 
    b = fruits.Banana()
```
```text
    当对子文件夹进行引用时，其形式又会出现如下更改。如package下的subpackage,subpackage中也要设计一个__init__.py的文件
    from package.subpackage import fruits

    a = fruits.Apple()   
    b = fruits.Banana()
```

### 两个常用的功能
```text
    1.dir        获取文件下包含多少功能
    2.__name__   获取文件名，适用于脚本的自动执行
```
```python
# fruits.py中补充
def tell_me():
    print('123')

print(dir(Apple))
print(__name__)
if __name__ == '__main__':
    tell_me()

# 运行
# python fruits.py
'''
['***（此处省略很多）, 'get_price', 'set_price']
__main__                                            # 这表明运行该文件时，其__name__就是__main__
123                                                 # 自动执行

'''
```