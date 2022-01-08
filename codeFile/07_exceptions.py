# task1: 捕捉异常，控制程序
'''
try:
    age= int(input('age:'))
except ValueError:
    print('please enter right value')
else:
    print('恭喜注册成功')
finally:
    print('程序结束')
# task2: 当try中包含文件资源的打开等操作，为保证资源的顺利释放，可增加finally语句
# 对待文件资源等，最好的方式还是采用with语句
'''

def cal(firstNum, secondNum):
    if secondNum <= 0:
        raise ValueError('Second Number error')
    else:
        return firstNum/secondNum

try:
    print(cal(6, 2))
    cal(5, 0)
except ValueError as error:
    print(error)
