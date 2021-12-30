## python学习--day09
**内容概述**
- 异常处理 Exceptions
****
重点知识
- 处理异常
- 抛出异常
****

### 处理异常
```text
try:
    code1
except error:                            #有异常执行此处
    handle
else:
    no error will run this part          #没有异常执行此处 
finally：
    code2                                #最后一定要执行的
    
#见代码示例1
```
```python
#代码1
try:
    age= int(input('age:'))
except ValueError:
    print('please enter right value')     #有异常执行此处
else:
    print('恭喜注册成功')
finally:
    print('程序结束')
'''
age:10
恭喜注册成功                #没有异常时，执行else语句
程序结束

age:aa
please enter right value
程序结束
'''
```

### 主动抛出异常
```text
采用rise关键字来抛出异常
见示例代码2
```
```python
#代码2
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

'''
3.0
Second Number error
'''
```
**异常的代价**
```text
   抛出异常的程序，通常在性能上会有较大的损耗
   一般而言，可以通过语句判断来避免抛出异常来优化程序 
```
```python
#代码3：对代码2进行优化
def cal(firstNum, secondNum):
    if secondNum <= 0:
        return None                  #raise ValueError('Second Number error')
    else:
        return firstNum/secondNum

ret= cal(5, 0)                      #去除异常的作用，优化程序执行效率
if ret == None:
    pass
else:
    print(ret)
```