## python学习--day01
### 变量
#### 命名规则
 - 由数字、字母、下划线组成
 - 不能由纯数字组成，也不能以数字开头
 - 不能采用python保留的关键字
 - 尽量避免中文
 - 命名有意义
 - 形式上尽量采用下划线或者驼峰命名
#### 综上，变量命名尽量有意义，规范.

### 常量
 - 一般默认全大写的变量为常量，不去做更改。

### 数据类型
 #### 数字型
 - int 整型
 - float 浮点型
 #### 文字
 - str 字符串
 - 单行表达  
  str1= 'abc'    
  str2= "abc"
 - 多行表达  
str3 = '''   
    大家好，   
    我是多行字符串，  
    谢谢。  
'''  
str4 = """   
    大家好，   
    我是多行字符串，  
    谢谢。  
"""
 #### 布尔值
 - bool  
  True/False

### 输入输出
#### 关于输入——>input
基本语法：
变量= input(提示语)  
注意：变量默认存储的类型为字符串  
因此需要做一个类型转换，其基本语法为：  
新变量= 新的类型（旧变量）  
实例如下
```python
def function01():
    a= input("请输入第一个数")
    b= input("请输入第二个数")
    print(a+b)
    
def function02():
    a = input("请输入第一个数")
    b = input("请输入第二个数")
    a= int(a)
    b= int(b)
    print(a+b)

function01()
"""
输出结果：
请输入第一个数10
请输入第二个数20
1020
"""

function02()
"""
输出结果：
请输入第一个数10
请输入第二个数20
30
"""
```
#### 关于输出——>print
参见使用实例

### 条件判断
基本语法：
```python
 #伪代码
#if第一类
 if 条件成立：
    执行代码      #注意缩进的必要

#示例代码
def check():
    money= 500
    if money>300:
        print('OK')
    print('check done')

check()
```
```python
 #伪代码
#if第二类
 if 条件成立：
    执行代码1      #注意缩进的必要
 else：
    执行代码2
#示例代码
def check():
    money= 100
    if money>300:
        print('Yes')
    else:
        print('No')
    print('check done')
check()
```
```python
 #伪代码
#if第三类
 if 条件1：
    执行代码1      #注意缩进的必要
 elif 条件2：
    执行代码2
 elif 条件3:
    执行代码3
 else:
    执行代码
#示例代码
def test():
    money= int(input('卡上余额'))
    if money>500:
        print('SSVIP')
    elif money>300:
        print('SVIP')
    elif money>100:
        print('VIP')
    else:
        print('None')
test()
```

### 循环
#### while循环
基本语法  
```python
 while 条件：  
    循环体    #注意冒号以及缩进
```
代码实例
```python
def sumAdd(num):
    if num<1:
        print("error")
    else:
        sum= 0
        n= 1
        while n<= num:
            sum= sum+n
            n= n+1
        print(sum)

ss= int(input('请输入数据'))
sumAdd(ss)
```
#### continue和break关键字
continue关键字作用——>结束本次循环，进入下一次循环   
break关键字作用——>结束当前循环体
pass关键字作用——>代码占位，一般不用，保证语法完整性

#### for循环
- 借助range函数进行计数类型的循环
- 直接对容器进行遍历  
代码实例
```python
def testFor(num):
    if str == type(num):
        for i in num:
            print(i)
    else:
        for i in range(int(num)):
            print(i)

testFor('abc')  #运行结果：a b c
testFor(5)      #运行结果：0 1 2 3 4
```
```python
#range的三种用法
for i in range(m):  #第一种表示[0, n）左闭右开区间
    print(i)

for i in range(m, n):  #第二种表示[m, n）左闭右开区间
    print(i)

for i in range(m, n, s):  #第一种表示[m, n）左闭右开区间，且间隔为s
    print(i)

#第三种测试代码
for i in range(1, 8, 2):
    print(i)   #结果：1 3 5 7
```