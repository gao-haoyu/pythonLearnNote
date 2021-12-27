## python学习--day07
**内容概述**
- 函数编程(中)
****
重点知识
- 变量的作用域&&函数的嵌套
- 闭包
- 装饰器
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
### 3.装饰器的雏形
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
'''
登录
新增人员
打印日志
登录
删除人员
打印日志
'''
```
### 4.装饰器的参数&返回值
```text
当装饰器需要传递参数时，因为装饰的函数其参数不确定，应采用如下的方式
def wrapper(fn):
    def inner(*args, **kargs):            #此处*args,**kagrs是接受所有位置参数&关键字参数
        #add operator
        fn(*args, **kargs)                #此处在调用中采用*args&**kargs是将元组，字典打散为正常参数
        #add operator                     #这个点可以参考函数的参数小节
    return inner
```
```text
当装饰器需要返回值的处理时，其情况如下：
def wrapper(fn):
    def inner(*args, **kargs):            
        #add operator
        ret= fn(*args, **kargs)       #此处的ret接收目标函数fn的返回值，并将其作为inner的返回值return
        #add operator                 #装饰器归根到底就是inner中对函数重新包装
        return ret                    
    return inner
```

### 5.装饰器的嵌套
```python
def wrapper1(fn):
    def inner(*args, **kargs):
        print('进入装饰器1')
        ret= fn(*args, **kargs)
        print('退出装饰器1')
        return ret
    return inner

def wrapper2(fn):
    def inner(*args, **kargs):
        print('进入装饰器2')
        ret= fn(*args, **kargs)
        print('退出装饰器2')
        return ret
    return inner
@wrapper1
@wrapper2
def target():
    print('目标函数')

target()

'''
进入装饰器1
进入装饰器2
目标函数
退出装饰器2
退出装饰器1
'''                  #多层装饰，其表达规律为层层嵌套
```
### 6.装饰器使用示例
```python
status= False
def wrapper(fn):
    def inner(*args, **kargs):
        global status
        if status== False:
            name= input('>>>')
            password= input('>>>')
            while 1:
                if name== 'admin' and password== '123':
                    status= True
                    break
                else:
                    print('信息有误')
        ret= fn(*args, **kargs)
        return ret
    return inner

@wrapper
def add():
    print('增加人员')

@wrapper
def delete():
    print('删除人员')

add()
delete()
'''
>>>admin
>>>123
增加人员
删除人员
'''
```