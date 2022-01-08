#函数的嵌套
#基本定义：函数里面再去定义函数
'''
def func1():
    def func2():
        pass
    pass
func1()

def func2():
    a= 10
    return a
b= func2()
print(b)

def func3():
    def func4():
        print(123)
    return func4
f= func3()
f()

def funcPass(f):
    f()

def test():
    print(1)

funcPass(test)


a= 10

def func():
    global a
    a= 20
func()
print(a)

def func1():
    b= 10
    def func2():
        nonlocal b
        b= 30
    func2()
    print(b)
func1()

def con():
    conVar= 10
    def manaVar():
        print(conVar)
        return conVar
    return manaVar

ret= con()
print(ret())


def wrapper(fn):
    def inner():
        print("登录")
        fn()
        print("打印日志")

    return inner

@wrapper
def func1():
    print('新增人员')

@wrapper
def func2():
    print('删除人员')

func1()
func2()


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