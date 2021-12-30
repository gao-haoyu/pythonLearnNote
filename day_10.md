## python学习--day10
**内容概述**
- 类 class
****
重点知识
- 类的基础知识
- 
****

### 类的基础知识
```text
基本格式：
    class 类名：
        类的公共成员变量
        构造函数中定义具体实例的成员变量
        成员函数（成员函数至少要有一个self的参数）
        
调用方式：
    object= class()
    
常用方法：
    isinstance(object, class)用来判断某一个对象是否属于某个类
```
```python
#code1
class Point:
    def test(self):
        print('testFunc')

P= Point()
P.test()
print(P, Point)
'''
testFunc
True
'''
```

### 构造函数
在实际使用中，我们的需求通常是有参构造，如何去写class中的构造函数？  ————>__init__()函数
```text
格式：
    class Point:
        def __init__(self, 参数...):
            #在此处可以直接定义实例的成员变量
            self.成员变量1= ...
            self.成员变量2= ...
#见示例code2
```
```python
#code2
class Point:
    def __init__(self, value1, value2):
        self.x= value1
        self.y= value2
    def draw(self):
        print(f'x= {self.x}, y= {self.y}')
        
p= Point(1,2)
print(p.x)
print(p.y)
p.draw()
'''
1
2
x= 1, y= 2
'''
```
### 类属性和实例属性的辨析
```python
class Point:
    default_color= 'red'                 #类属性
    def __init__(self, value1, value2):
        self.x= value1
        self.y= value2
    def draw(self):
        print(f'point({self.x}, {self.y})')
```
**特点分析**
当采用类属性之后，其调用可以采用类名直接操作
当采用类名调用并更改属性后，其所有的实例均随之改变
```python
p1= Point(1,2)                   
print(p1.default_color)         #red      依据类属性生成的对象其颜色为初始的red
Point.default_color= 'blue'          #调用类名， 更改类属性
print(p1.default_color)         #blue     依据新的类属性，更改自身原有属性

p2= Point(3,4)
print(p2.default_color)         #blue     依据新的类属性
p2.default_color= 'red'              #更改自身的
print(p2.default_color)         #red    

p3= Point(5,6)
print(p3.default_color)         #blue   #p3并不因为p2而改变，只认Point属性
```
**一种便捷的默认初始化方式zero**
```python
class Point:
    default_color= 'red'
    def __init__(self, value1, value2):
        self.x= value1
        self.y= value2

    @classmethod
    def zero(cls):                  #@是固定写法
        return cls(0, 0)            #cls也是固定写法
                                    #通过这种方式，返回一个初始化对象
    def draw(self):
        print(f'point({self.x}, {self.y})')
```

### magic method
```text
特点：
    __functionName__
常见情况：
    __str__()   :一般其作用是将对象以字符串的形式输出，便于读取
    __eq__()    :编写判别是否相等
    __cmp__()   :比较大小
```
```python
class Point:
    default_color= 'red'
    def __init__(self, value1, value2):
        self.x= value1
        self.y= value2

    @classmethod
    def zero(cls):
        return cls(0, 0)
    
    def __str__(self) :                          #进行格式转换
        return f'Point({self.x}, {self.y})'
    
    def __eq__(self, other):                     #进行相等判断
        return self.x== other.x & self.y== other.y
    
    def draw(self):
        print(f'point({self.x}, {self.y})')

p= Point.zero()       #便捷初始化方案
print(p.__str__())    #第一种调用方法
print(str(p))         #第二种调用方法，推荐
'''
Point(0, 0)
Point(0, 0)
'''
```
