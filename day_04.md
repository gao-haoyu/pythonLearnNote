## python学习--day04
**内容概述**
- 字典dict
- 字节Byte+编码方式
- 运算符
****
重点知识  
- 字典基本定义
- 字典增删改查
- 字典循环嵌套
- 字典循环删除
- 编码方式
- Byte的用法场景
- 常见运算符操作场景
****
### 字典
### 1.基本定义
```text
定义：以键值对形式存储的一种容器，其常见场合为通过键来获取值。键必须为可哈希的数据类型，值不做任何要求。
形式： dic= {key1: value1, key2: value2}
```
```python
dic = {'Amy': 90, 'Bob': 93, 'Cindy': 88}
print(dic['Bob'])
'''
93
'''
```

### 2.字典的增删改查
```text
初始化一个空字典：dic= dict()

新增操作：
直接dic[key]= value

修改操作:
dic[key]= newValue

删除操作：
dic.pop(key)   #这一种比较好
del dic[key]

查找操作：
val= dic[key]   #当明确key存在时，采用这个查询方式， 当key不存在采用该方式，程序报错。
val= dic.get(key)  #当key存在返回value， 当key不存在返回None
```

```python
#应用案例：分数查询系统
dic = {'Amy': 90, 'Bob': 93, 'Cindy': 88}
name= input('Please enter your name')
score= dic.get(name)
if score == None:       #此处也可写作 if score is None:
    print('Not exist')
else:
    print(score)

'''
Please enter your name: Cindy
88
Please enter your name: Deff
Not exist
'''
```

### 3.字典的循环&嵌套
**字典循环遍历的四种方案**
```text
#Plan_One:循环key，借助key得value
    for key in dic :
        print(dic[key])
    
#Plan_Two：将keys全转为列表存储
    keyLst= list(dic.keys())

#Plan_Three：将values全转为列表存储
    valueLst= list(dic.values())

#Plan_Four：直接循环key,value
    for key,value in dic.items():
        print(key, value)
```
**关于第四种遍历方式的解释**

```python
# 原型：
import dict

for item in dict.items():
    print(item)               #此时为元组数据类型
    #print(type(item))        #<class 'tuple'>
'''
('Amy', 90)
('Bob', 93)
('Cindy', 88)
'''

#元组类型具有如下用法
a, b= item           #保证item中只有两个元素
#此时a,b会被自动赋值为元组的第一个和第二个数据。
#所以形式转换为上述第四种方案
```

**字典的嵌套**
```text
厘清逻辑顺序，直接[]获取相应的元素。
通过代码示例理解,就是单纯的嵌套关系
```
```python
dic= {
    "teacherA":{'name': 'Henry',
              'students':{'AA': 85, 'BB': 88}},
    'teacherB':{'name': 'Harris',
              'students':{'CC': 86, 'DD': 87}},
}
print(dic['teacherA']['name'])
print(dic['teacherB']['students']['CC'])

'''
Henry
86
'''
```

### 4.字典的循环删除
**同列表的循环删除类似，字典在循环中删除数据亦不可取**
**可以采用的方法，依然是事先采用列表记录key值，循环后进行删除**
```python
#删除不及格人员(小于60)
dic= {'AA': 15, 'BB': 60, 'CC': 85, 'DD': 23}
lst = list()
for k, v in dic.items():
    if v< 60:
        lst.append(k)
for name in lst:
    dic.pop(name)
print(dic)

'''
{'BB': 60, 'CC': 85}
'''
```
****

### 编码方式
```text
编码方式溯源：
ASCII码：1个字节，8bit
ANSI——>gbk：2个字节(byte),16bit
Unicode：4个字节，空间资源浪费，在此基础上衍生出UTF-8
UTF-8：动态可变
    英文：1Byte
    欧洲：2Byte
    中文：3Byte
```
**可以看到gbk是依托ANSI标准，UTF-8依托于Unicode。因此不可能将gbk的编码和UTF-8直接转化**

### Byte
```text
重要的点：
encode('编码方式')    字符——>Byte
decode('解码方式')    Byte——>字符
```

```python
#如何将gbk编码得到的Byte转为
s= '测试'
b1= s.encode('gbk')
b2= s.encode('UTF-8')
print(b1)
print(b2)

s1= b1.decode('gbk')
print(s1.encode('UTF-8'))
```

*****
### 运算符
- 算术运算符
    ```text
      + - * / 加减乘除
      %(取余)  
      //(整除)
    ```
- 比较运算符
    ```text
    > < >= <= == !=
    ```
- 赋值运算符
    ```text
    = += -= *= ...
    ```
  ```python
    #两数互换
    a= 20
    b= 10
    #常规写法
    temp= a
    a= b
    b= temp
    
    #纯代数方法
    a= a-b
    b= a+b
    a= b-a
    
    #python特有方案
    b, a= a, b    #解构写法
    ```
- 逻辑运算符
    ```text
    与——> and
    或——> or
    非——> not
    注意：多段逻辑组合，采用括号划分区域，防止歧义
    当多逻辑无括号时，其运算顺序为：先括号，再not，再and，再or
    ```
- 成员运算符
    ```text
    in      包含
    not in  不包含
    ```
    ```python
    lst= [1, 2, 3]
    print(3 in lst)       #True
    print(4 not in lst)   #True
    ```