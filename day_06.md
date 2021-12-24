## python学习--day06
**内容概述**
- 函数编程
****
重点知识  
- 函数的基本概念
- 函数的参数
- 函数的返回值
- 部分内置函数
****

### 1.函数基本概念
```text
定义：函数就是对某一部分功能代码块进行封装
形式
def 函数名(参数1, 参数2):
    函数体

#见代码1
```
```python
#代码1：应用示例
def cal(a, opt, b):
    if opt == '+':
        print(f'{a}+{b}= {a+b}')
    elif opt == '-':
        print(f'{a}-{b}= {a - b}')
    elif opt == '*':
        print(f'{a}*{b}= {a * b}')
    elif opt == '/':
        print(f'{a}/{b}= {a / b}')
    else:
        print('check your input')

cal(5, '+', 3)
cal(5, '-', 3)
cal(5, '*', 3)
cal(5, '/', 3)
cal(5, '^', 3)

'''
5+3= 8
5-3= 2
5*3= 15
5/3= 1.6666666666666667
check your input
'''
```
****
### 2.函数的参数
**实参**
```text
实参的分类
位置参数：依照位置顺序严格传入参数
关键字参数：传参的同时标注是哪一个形参
混合参数：位置和关键字参数都有，但一定要保证位置参数全部在前，且所有参数均被赋值

#见代码2
```
```python
#代码2：实参示例
def testAgr(first, second, third):
    print(first, second, third)

#第一种调用
testAgr(1, 2, 3)
#第二种调用
testAgr(first= 1, second= 2, third= 3)
#第三种调用
testAgr(1, 2, third= 3)

'''
1 2 3
1 2 3
1 2 3
'''
```
**形参**
```text
形参的分类
位置参数 ：按位置设置形参
默认值参数：为形参设计默认值，简化函数调用   当位置参数和默认值参数同时存在时，要求位置参数全部在前。

动态传参：
    动态传位置参数——>采用*args即可
    动态传关键字参数——>采用**args即可
    
见代码3
```
```python
#代码3：形参示例
def testDynamicpositonArgs(*nums):
    print(type(nums))
    print(nums)

def testDynamicKeyArgs(**nums):
    print(type(nums))
    print(nums)

testDynamicpositonArgs(1, 2, 3, 4 ,5)
testDynamicKeyArgs(fir= 1, sec= 2, third= 3)
'''
<class 'tuple'>
(1, 2, 3, 4, 5)
<class 'dict'>
{'fir': 1, 'sec': 2, 'third': 3}
'''
```

`形参的顺序应遵循：位置参数, *args, 默认参数, **args`  

**参数的补充知识**
```python
#代码4：特殊用法
def testPoint(*args, **margs):
    print(args)
    print(margs)

lst= [1, 2, 3, 4, 5]
dic= {'a':1, 'b': 2, 'c': 3}
testPoint(*lst)
testPoint(**dic)
testPoint(*lst, **dic)      # *, **在实参调用中可以将容器打散为位置参数

'''
(1, 2, 3, 4, 5)
{}
()
{'a': 1, 'b': 2, 'c': 3}
(1, 2, 3, 4, 5)
{'a': 1, 'b': 2, 'c': 3}
'''
```
****
### 3.函数的返回值
```text
函数默认返回None
采用return关键字写返回值
多个返回值时，返回的为一个元组
```

### 4.内置函数
```python
#进制转换
bin(18) #二进制  0b10010
oct(18) #八进制  0o22
hex(18) #16进制  0x12
```
```python
#数学运算
abs(-10)    #取绝对值  10
pow(10, 3)  #计算次幂 1000
max([5, 7, 9, 11, 45, 23])  #得到最大值  45
min([5, 7, 9, 11, 45, 23])  #得到最小值  5
sum([5, 7, 9, 11, 45, 23])  #得到和     100    
```
```python
#字符串 format,  chr, ord
a= 18
print(format(a, '08b'))   #00010010  补齐8位
b= '中'
c=ord(b)                     
print(c)                  #20013    unicode码
print(chr(c))             #中        反解析
```
```python
#enumerate any all
enumerate()   #同时获取index和value
any()         #逻辑or处理
all()         #逻辑and处理

#代码
lst= ['a', 'b', 'c']
for index, value in enumerate(lst):
    print(index, value)
'''
0 a
1 b
2 c
'''
```
