## python学习--day03
**内容概述**
- 列表list
- 元组tuple
- 集合set
****
重点知识  
- list中append,remove,列表的遍历 
- tuple的不可变指的是内存地址
- set的增删改查&用于去重
****

### 1.基本概念
- 定义：存储元素的一种容器，采用[]表示
- 特点：可以放置任意类型，任意嵌套(见示例)
```python
#示例代码
aList= [1,2,3, "abc", 'a',['b', 'c']]
print(f'长度为{len(aList)}')
for c in aList:
    print(c)
#运行结果
'''
长度为6
1
2
3
abc
a
['b', 'c']
'''
```

### 2.索引和切片
类比于字符串的操作，在列表中都是通用的。
```python
#示例代码
aList= [1,2,3, "abc", 'a',['b', 'c']]

print(aList[3])   
print(aList[0:3])
print(aList[::3])
print(aList[::-1])

#运行结果
'''
abc
[1, 2, 3]
[1, 'abc']
[['b', 'c'], 'a', 'abc', 3, 2, 1]
'''
```

### 3.列表的增删改查
**增加元素append, insert, extend**
````python
#代码示例
lst= ['a', 'b', 'c']

#append:追加元素, 参数为data
lst.append('d')
print(lst)
#['a', 'b', 'c', 'd']

#insert:插入元素， 参数为index， data
lst.insert(0, '0')
print(lst)
#['0', 'a', 'b', 'c', 'd']

#extend:合并两个列表, 参数为list
subLst= ['e', 'f']
lst.extend(subLst)
print(lst)
#['0', 'a', 'b', 'c', 'd', 'e', 'f']
````

**删除元素pop,remove**
````python
#代码示例
lst= [1, 2, 3]
#pop:弹出某一位置的元素，参数为index,返回弹出的元素
ret= lst.pop(2)
print(lst)
print(ret)
#[1, 2]
#3

#remove:移除某一个元素，参数为data，不返回
lst.remove(2)
print(lst)
#[1]
````

**修改&查找元素，直接采用索引**
```python
#code example
lst= [1, 2, 3]
print(lst)
lst[0]= 0
ret= lst[0]
print(ret)

#[1, 2, 3]
#0
```

### 4.code_practice
- Q:将列表['张三','张四','张五','王一','王二','王六']中张姓全部改换为王姓
- A:
```python
#方案一：只在循环体里修改&打印
def func(lst):
    for name in lst:                       #不需要获取索引的遍历
        if(name.startswith("张")):
            name= name.replace("张", "王")  #此处采用replace也不太严谨，有错误的可能
        print(name)

        
#方案二：彻底的修改
def func2(lst):
    for i in range(len(lst)):              #需要获取索引的遍历
        name= lst[i]
        if(name.startswith("张")):
            newName= "王"+name[1:]
            lst[i]= newName
```

```python
#代码测试
lst= ['张三','张四','张五','王一','王二','王六']

func(lst)
print(lst)

func2(lst)
print(lst)
'''
王三
王四
王五
王一
王二
王六
['张三', '张四', '张五', '王一', '王二', '王六']
['王三', '王四', '王五', '王一', '王二', '王六']
'''
```

### 5.列表的补充操作
- 列表的排序
    ```python
    lst= [11, 12, 5 ,6 ,3]
    lst.sort()
    print(lst)
    lst.sort(reverse= True)
    print(lst)
    #[3, 5, 6, 11, 12]
    #[12, 11, 6, 5, 3]
    ```
  
- 列表的嵌套
    ```python
    lst1= [1,'a',['b',['c']]]
    ret= lst1[2][1][0]
    print(ret)
    #c
    ```
- 列表的循环删除
    ```python
    #容易出现漏删的情况，这个地方要仔细应对
    #漏删案例
    lst2= [1,2,2,3,4,5]
    for it in lst2:
        if it == 2:
            lst2.remove(it)
    print(lst2)
  
    #结果：[1, 2, 3, 4, 5]
    ```
    ```python
    #正确的做法，先记录再删除
    lst2= [1,2,2,3,4,5]
    census= []
    for it in lst2:
        if it == 2:
            census.append(it)
    
    for it in census:
        lst2.remove(it)
    print(lst2)
  
    #结果：[1, 3, 4, 5]
    ```
****
### 元组tuple
**定义**
```python
#语法形式：小括号()
tu= ('a', 'b', 'c')
```

**要点**
- 当元组中只有一个数据时，要采用额外的操作。
```python
tu1=('a')
tu2=('a',)         #当只有一个元素时，额外加一个逗号，保证类型
print(type(tu1))
print(type(tu2))

'''
<class 'str'>
<class 'tuple'>
'''
```
- 内部元素不可被重新赋值，不可改变内存地址。
```python
#其含义是不可以更改内部的元素地址，参见代码示例
tu=('a', 'b', 'c',['d'])
print(tu)
tu[3].append('e')    #此处通过，因为tu[3]这一次的更改，并不改变原本的内存地址
print(tu)
tu[0]= 's'           #此处报错：'tuple' object does not support item assignment

'''
('a', 'b', 'c', ['d'])
('a', 'b', 'c', ['d', 'e'])
Traceback (most recent call last):
  File "C:\Users\Gao\PycharmProjects\pythonProject\tuple.py", line 5, in <module>
    tu[0]= 's'
TypeError: 'tuple' object does not support item assignment
'''
```
****
### 集合set
**定义**
```python
#空集合的创建
s= set()
s1= {'a','b','c'}   #初始化一个集合，实际使用中也是{}表示集合
```

**特点**
```python
#存储元素无序 print(s1)——> {'b', 'c', 'a'}
#内部不可放置不能哈希的数据类型如：list, set, dict等
```

**常见操作**
```python
#增删改查
s2.add('d')      #增
s2.remove('d')   #删

s2.remove('b')
s2.add('b1')    #改，需要先删后增

for it in s2:  
    print(it)   #查询，只有遍历
```

**补充操作**
- 交集，并集，差集
- 去重
```python
#代码示例
s1= {1, 2, 3, 4, 5}
s2= {3, 4, 5 ,6 ,7}
print(s1&s2)             #交集
print(s1|s2)             #并集
print(s1-s2)             #差集

'''
{3, 4, 5}
{1, 2, 3, 4, 5, 6, 7}
{1, 2}
'''
```

- 因为set中不包含重复元素，利用这一性质直接去重
```python
s1= {1, 2, 3, 4, 5}
s2= {3, 4, 5 ,6 ,7}

lst= list(s1)+ list(s2)
print(lst)

print(set(lst))
print(list(set(lst)))

'''
[1, 2, 3, 4, 5, 3, 4, 5, 6, 7]
{1, 2, 3, 4, 5, 6, 7}
[1, 2, 3, 4, 5, 6, 7]
'''
```
