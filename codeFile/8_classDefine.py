class Point:
    default_color = 'red'

    def __init__(self, value1, value2):
        self.x = value1
        self.y = value2

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __str__(self):  # 进行格式转换
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):  # 进行相等判断
        return self.x == other.x & self.y == other.y

    def __gt__(self, other):   # 大于判断
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


'''
clas TagCloud:...
tag= TagCloud()
len(tag)
tag[key]
for it in tag:
    print(it)'''
class TagCloud:
    def __init__(self):
        self.__dic = {}

    def add(self, keyword):
        keyword = keyword.lower()
        if self.__dic.get(keyword):
            self.__dic[keyword] += 1
        else:
            self.__dic[keyword] = 1

        # 此处可以程序优化为  ：：： self.__dic[keyword] = self.__dic.get(keyword, 0) + 1

    def __getitem__(self, item):
        return self.__dic[item.lower()]
        # 此处可以程序优化  ：：： return self.__dic.get(item.lower(), 0)

    def __setitem__(self, key, value):
        self.__dic[key.lower()] = value

    def __iter__(self):
        return iter(self.__dic.items())        # 此处返回items，才能保证准确地拿到所有的数据

    def __len__(self):
        return len(self.__dic)

'''
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

class Product:
    def __init__(self, val):
        if val > 0:
            self.__price = val
        else:
            return ValueError

    def setPrice(self, val):
        if val > 0:
            self.__price = val
        else:
            return ValueError

    def getPrice(self):
        return self.__price


class Product2:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        if val > 0:
            self.__price = val
        else:
            raise ValueError('wrong')

p1= Product2(-10)