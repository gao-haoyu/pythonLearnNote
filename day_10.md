## python学习--day10
**内容概述**
- 类 class
****
重点知识
- 类的基础知识
- 构造函数，zero函数封装初始化对象
- 类成员变量和实例成员变量
- magic method   十分重要！！！
- 类中封装容器
- 私有成员属性
- 为类设置属性量
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
    __gt__()    :大于判断
    
    算术运算相关： add(+) sub(-)  mul(*)  div(/)  #格式见代码
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
    
    def __gt__(self, other):                     # 大于判断
        return self.x > other.x and self.y > other.y
    
    def __add__(self, other):  # 自定义加法
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):  
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass
    
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

### 自定义容器(封装一个含有容器的类)
```text
# 定义一个类可以完成类似容器的若干操作
# 具体需求接口
clas TagCloud:...
tag= TagCloud()
len(tag)
tag[key]
for it in tag:
    print(it)
```

```python
#具体实现代码
class TagCloud:
    def __init__(self):                 # 内置容器
        self.dic = {}

    def add(self, keyword):             # 添加元素
        keyword = keyword.lower()
        if self.dic.get(keyword):
            self.dic[keyword] += 1
        else:
            self.dic[keyword] = 1

        # 此处可以程序优化为  ：：： self.dic[keyword] = self.dic.get(keyword, 0) + 1

    def __getitem__(self, item):       # 利用[]获取value
        return self.dic[item.lower()]
        # 此处可以程序优化  ：：： return self.dic.get(item.lower(), 0)

    def __setitem__(self, key, value): # 利用[]来赋值value
        self.dic[key.lower()] = value

    def __iter__(self):                # 返回迭代器用于for循环
        return iter(self.dic.items())        # 此处返回items，才能保证准确地拿到所有的数据

    def __len__(self):
        return len(self.dic)
```
```python
#测试代码
cloud = TagCloud()
cloud.add('python')
cloud.add('python')
cloud.add('Python')
cloud['java'] = 3
cloud['go'] = 2
print(len(cloud))
print(cloud['go'])
for it in cloud:
    print(it)

'''
3
2
('python', 3)
('java', 3)
('go', 2)
'''
```

### 私有成员属性
```text
# 需求Q:在上面的TagCloud中内部维护了一个记录数据的字典。在设计中，并不希望用户直接访问到该内部容器。
# 方案A:针对上述需求，我们可以采用私有属性声明，技法上采用__name来设定私有成员
```
```python
#上述代码的优化，将dic设置为私有成员
class TagCloud:
    def __init__(self):                 # 内置容器
        self.__dic = {}

    def add(self, keyword):             # 添加元素
        keyword = keyword.lower()
        self.__dic[keyword] = self.__dic.get(keyword, 0) + 1

#这种方式之后，生成的实例对象无法直接调用__dic，实现私有化
#记录一个技法： 批量修改变量名
#ctrl+R  调出替换框
#上框填写原来的变量名， 下框填写新变量名
#replace all 替换所有
```

### 设计属性特征 property
```text
需求：我们希望class有一个属性，对其读取和赋值有单独的管理
方案：采用property来定义这个变量

示例：将Product类中的price设置为property，希望price这个属性大于0
```

```python
#代码1： 采用一般思路控制
class Product:
    def __init__(self, val):
        if val > 0:
            self.__price = val
        else:
            raise ValueError('wrong')
        
    def setPrice(self, val):
        if val > 0:
            self.__price = val
        else:
            raise ValueError('wrong') 
    
    def getPrice(self):
        return self.__price

#具体使用时
p= Product(10)
p.getPrice()       #获取price
p.setPrice(20)     #更改price
```
```python
#代码2：利用property来优化
class Product2:
    def __init__(self, price):
        self.price = price                 #在构造函数中，对属性量price来直接进行赋值

    @property                 
    def price(self):                       #定义属性量为price
        return self.__price

    @price.setter                          #定义属性量赋值的管理
    def price(self, val):
        if val > 0:
            self.__price = val
        else:
            raise ValueError('wrong')

#具体使用时
p= product2(10)         #具有正数判断
p.price  #直接是price
p.price= 20 #更改price ，具有正数判断
```