## python学习--day07
**内容概述**
- 函数编程(下)
****
重点知识
- 迭代器
- 生成器
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
```text
生成器本质上是一个迭代器！！！

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