## python学习--day08
**内容概述**
- 函数编程(下)
****
重点知识
- 迭代器
- 生成器     ——>生成器函数&生成器表达式
- 匿名函数   ——>lambda表达式
- 内置函数   ——>sorted、filter、map函数
****

### 1.迭代器
```text
迭代器：iterator
类比于C++来看，其功能是一致的.

#获取迭代器的方式
    内置函数：iter()
    成员函数：__iter__()

#获取迭代器指向数值的方式
    内置函数：next()
    成员函数：__next__()
  
#自身特性
    1.自身可迭代，迭代器也能用for循环
    2.占用内存小(指针的概念，只记录位置)
    3.只能向前
具体使用见代码1
```
```python
#代码1
ss= '123'
it= iter(ss)             #方式1获取

print(next(it))          #方式1读值
print(next(it))
print(next(it))
print(next(it))
'''
1
2
3
Traceback (most recent call last):
    print(next(it))             
StopIteration               #当超出范围是，会报StopIteration错误
'''
ss= '123'
it= ss.__iter__()          #方式2获取

print(it.__next__())       #方式2读值
print(next(it))            #可以混用
print(it.__next__())
'''
1
2
3
'''
```
```python
#代码2
#拆解for循环的代码原理
v= list()
for it in v:
    #内部具体操作
    pass

#拆解之后
it= v.__iter__()
while 1:
    try:
        val= next(it)
        #具体操作
    except StopIteration:
        break
```
### 2.生成器
**生成器本质上是一个迭代器！！！**
```text
#生成器的创建方式
    1.生成器函数
    2.生成器表达式
    
#生成器函数
    1.形式特点：采用yield代替return
    2.运行特点：将函数改制为类似于迭代器的运行，可以实现按步执行。
    参考代码3
```
```python
#代码3
#生成器函数的使用
def func():                 #定义一个生成器函数
    print(1)
    yield 2
    print(3)
    yield 4

#当采用如下调用时
it= func()   #此时已经成为了一个生成器
it.__next__()
it.__next__()
'''
1
3
'''

#当接受其返回值时，也可正常运行,说明yield既实现了逐步运算又有return的功能
it= func()   #此时已经成为了一个生成器
print(it.__next__())
print(it.__next__())
'''
1
2
3
4
'''
```
```python
#代码4
#生成器的案例使用
#需求：希望以10个为单位，拿到10000个数据
def func():
    lst= []
    for i in range(10000):
        lst.append(f'No.{i}')
        if len(lst)== 10:
            yield lst
            lst= []

it= func()
print(it.__next__())
print(it.__next__())         
'''
['No.0', 'No.1', 'No.2', 'No.3', 'No.4', 'No.5', 'No.6', 'No.7', 'No.8', 'No.9']
['No.10', 'No.11', 'No.12', 'No.13', 'No.14', 'No.15', 'No.16', 'No.17', 'No.18', 'No.19']
'''
```

### 3.推导式
```text
一种特殊的写法用于简化代码
    1.列表推导式       ——>[data for if] 
    2.集合推导式       ——>{data for if}
    3.字典推导式       ——>{k:v  for if}

#使用实例见下列代码
```
```python
#代码5   列表推导式&&集合推导式&&字典推导式

#task1: 生成一个0-9的列表
lst= [i for i in range(10)]
print(lst)                   #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#task2: 生成1、3、5、7、9列表
lst= [i for i in range(10) if i%2 == 1]
print(lst)                   #[1, 3, 5, 7, 9]

#task3: 生成字符串列表
lst= [f'数据{i}' for i in range(10)]
print(lst)  
#['数据0', '数据1', '数据2', '数据3', '数据4', '数据5', '数据6', '数据7', '数据8', '数据9']

#task4：将小写转为大写
lst1= ['aa', 'bb', 'cc', 'dd']
lst2= [it.upper() for it in lst1]
print(lst2)
#['AA', 'BB', 'CC', 'DD']


#task5：生成一个0-9的数字集合
st= {i for i in range(10)}
print(st)
#{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


#task6：将一个列表，以索引为key，值为value构建一个字典
lst= ['aa', 'bb', 'cc', 'dd']
dic= {i:lst[i] for i in range(len(lst))}
print(dic)
#{0: 'aa', 1: 'bb', 2: 'cc', 3: 'dd'}
```

### 4.生成器表达式
```text
形式：
    gen= (数据 for循环 if判断)   #其得到的是一个生成器
    使用方式见代码2
```
```python
#代码6  生成器使用案例
gen= (i for i in range(5))
print(gen.__next__(), end=' ')        #此处end参数的更改，只是为了显示的效果
print(gen.__next__(), end=' ')
print(gen.__next__(), end=' ')
print(gen.__next__(), end=' ')
print(gen.__next__(), end=' ')
'''
0 1 2 3 4 
'''

#生成器也可采用循环的方式遍历
gen= (i for i in range(5))
for it in gen:
    print(it, end=' ')
'''
0 1 2 3 4 
'''

#将生成器同list进行转换
gen= (i for i in range(5))
lst= list(gen)
print(lst)
'''
[0, 1, 2, 3, 4]
'''
```

### 5.匿名函数(lambda表达式)
```text
语法规则
    变量= lambda 参数1， 参数2, ... : 函数体
```
```python
#代码7： lambda表达式
fn= lambda a, b: a+b
print(fn(2,3))
'''
5
'''
```

### 6.内置函数
**重点函数：sorted filter map**
```text
#第一部分：locals globals zip
作用
    locals:   以字典的形式，将所有当前作用域变量返回
    globals： 以字典的形式，将所有全局变量返回
    zip：     将多个可迭代的内容合并在一起
```

```python
#代码8：内置函数zip, locals, globals
lst1= ['Allen', 'Bob', 'Cindy']
lst2= ['一年级','二年级','二年级']
lst3= [6, 7, 7]
rest= zip(lst1, lst2, lst3)       #此时是形成一个迭代器
rest= list(rest)
print(rest)
'''
[('Allen', '一年级', 6), ('Bob', '二年级', 7), ('Cindy', '二年级', 7)]
'''
```
#### 6.1 sorted函数
```text
函数原型
    sorted(iter, key, reverse)
    iter     ——> 含有迭代器的容器
    key      ——> 排序规则,其运行机制是，将迭代器指向的每一项都运行该规则之后得到一个数，并依据此数排序
    reverse ——> 是否翻转
应用案例
    见代码9
```
#### 6.2 filter函数
```text
筛选
函数原型
    filter(rule, iter)
    rule  ——>筛选规则，其运行机制是，将每一项运行该规则后，判定是否为真，若为真则保留
    iter  ——>含有迭代器的容器
应用案例
    见代码9
```
#### 6.3 map函数
```text
映射
函数原型
    map(rule, iter)
    rule  ——>映射规则，其运行机制，将每一项运行该规则后，保留结果
    iter  ——>含有迭代器的容器
```

```python
#代码9

#sorted实例
#task1：依据名称长短排序
lst=['明', '张三', '李二狗', '王四麻子']
lst= sorted(lst, key= lambda a: len(a))
print(lst)
'''
['明', '张三', '李二狗', '王四麻子']
'''
#若设置reverse属性，则会翻转
lst=['明', '张三', '李二狗', '王四麻子']
lst= sorted(lst, key= lambda a: len(a), reverse= True)
print(lst)
'''
['王四麻子', '李二狗', '张三', '明']
'''

#task2：复杂结构下的排序
lst= [
    {'name': 'Allen', 'age': 18, 'salary': 100},
    {'name': 'Bob', 'age': 20, 'salary': 600},
    {'name': 'Cindy', 'age': 19, 'salary': 200},
    {'name': 'David', 'age': 22, 'salary': 500}
]
lst1= sorted(lst, key= lambda dic: dic['age'])       #依据年龄排序
print(lst1)
'''
[{'name': 'Allen', 'age': 18, 'salary': 100}, 
 {'name': 'Cindy', 'age': 19, 'salary': 200}, 
 {'name': 'Bob', 'age': 20, 'salary': 600}, 
 {'name': 'David', 'age': 22, 'salary': 500}]
'''
lst2= sorted(lst, key= lambda dic: dic['salary'])       #依据薪水排序
print(lst2)
'''
[{'name': 'Allen', 'age': 18, 'salary': 100}, 
 {'name': 'Cindy', 'age': 19, 'salary': 200}, 
 {'name': 'David', 'age': 22, 'salary': 500}, 
 {'name': 'Bob', 'age': 20, 'salary': 600}]
'''

#filter案例
#task:筛选salary大于300的
lst= [
    {'name': 'Allen', 'age': 18, 'salary': 100},
    {'name': 'Bob', 'age': 20, 'salary': 600},
    {'name': 'Cindy', 'age': 19, 'salary': 200},
    {'name': 'David', 'age': 22, 'salary': 500}
]
lst1= list(filter(lambda dic: dic['salary']> 300 , lst)) #filter之后是一个迭代器，因此采用list转型
print(lst1)
'''
[{'name': 'Bob', 'age': 20, 'salary': 600}, 
 {'name': 'David', 'age': 22, 'salary': 500}]
'''


#map案例
#task: 对列表元素进行映射
lst= [1, 2, 3, 4, 5]
lst1= list(map(lambda x: x*x , lst))
print(lst1)
'''
[1, 4, 9, 16, 25]
'''
```