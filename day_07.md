## python学习--day07
**内容概述**
- 函数编程(上)
****
重点知识
- 变量的作用域&&函数的嵌套
- 闭包
- 装饰器
- 迭代器
- 生成器
- 推导式
- 匿名函数
- 内置函数(下)
****

### 1.变量的作用域&&函数的嵌套
```text
python中采用缩进来控制作用域，类似于C++中{}
分为全局变量&局部变量

当需要在全局中调用局部变量，采用return来返回。
见代码1
```
```python
#代码1
#常规变量
def func2():
    a= 10
    return a
b= func2()
print(b)             #10

#将函数作为变量进行返回
def func3():
    def func4():
        print(123)
    return func4
f= func3()
f()                  #123， 此处相当于调用func4

#将函数作为参数进行传递
def funcPass(f):
    f()
def test():
    print(1)
funcPass(test)       #1, 此处将函数作为参数传递
```
**函数名本质上就是一个变量名，都表示一个内存地址！！！**

```text
#当需要在函数内部使用非当前的局部变量时，可以采用的技术手段
1.global关键字，在局部引入全局变量
2.nonlocal关键字
在局部引入外部的局部变量，向外找一层，没有继续向外，直到全局(不包括全局)

见代码2
```
```python
#代码2：global和nonlocal

a= 10
def func():
    global a      #此处若不采用global声明，会被默认为局部变量
    a= 20
func()
print(a)           #20

def func1():
    b= 10
    def func2():
        nonlocal b  #此处采用nonlocal声明，会逐层向上寻找局部变量
        b= 30
    func2()
    print(b)
func1()            #30
```
### 2.闭包
```text
形式：内层函数对外层函数局部变量的使用，此时内层函数称为闭包函数
作用：
    1.可以让一个常量常驻内存，有全局变量的效果
    2.可以避免维护的局部变量被外部任意修改，只能通过函数内部来控制
    
见代码3
```
```python
#代码3：闭包
def con():
    conVar= 10
    def manaVar():
        print(conVar)
        return conVar
    return manaVar
ret= con()          #通过这种方案，外界不可能直接拿到conVar
print(ret())        #想要修改conVar，也只能借助manaVar函数
         #假设将print语句去除，这个闭包的功能就是维护conVar数据的纯洁性
'''
10
10
'''
```
### 3.装饰器
```text
定义：本质上是一个闭包
作用：对目标函数进行功能扩展，不改变源代码
形式：
def wrapper(fn):
    def inner():
        # add operator
        fn()
        # add operator
    return inner
    
通过示例来理解其作用，见代码4
```
```python
#代码4：装饰器
def wrapper(fn):
    def inner():
        print("登录")
        fn()
        print("打印日志")
    return inner

def func1():
    print('新增人员')
    
def func2():
    print('删除人员')

#先思考下面操作的意义
func1= wrapper(func1)     #将inner重新赋值给func1
func2= wrapper(func2)     #将inner重新赋值给func2

func1()
func2()
'''
登录
新增人员
打印日志
登录
删除人员
打印日志
'''
#采用装饰器增加功能并返回，保证后续操作

#实际中的写法为@wrapper，如下：
def wrapper(fn):
    def inner():
        print("登录")
        fn()
        print("打印日志")

    return inner

@wrapper                  #调用wrapper进行修饰
def func1():
    print('新增人员')

@wrapper
def func2():
    print('删除人员')

func1()
func2()
```


