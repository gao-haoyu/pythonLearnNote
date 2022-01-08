'''
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

def testAgr(first, second, third):
    print(first, second, third)

#第一种调用
testAgr(1, 2, 3)
#第二种调用
testAgr(first= 1, second= 2, third= 3)
#第三种调用
testAgr(1, 2, third= 3)

def testDynamicpositonArgs(*nums):
    print(type(nums))
    print(nums)

def testDynamicKeyArgs(**nums):
    print(type(nums))
    print(nums)

testDynamicpositonArgs(1, 2, 3, 4 ,5)
testDynamicKeyArgs(fir= 1, sec= 2, third= 3)


def testPoint(*args, **margs):
    print(args)
    print(margs)

lst= [1, 2, 3, 4, 5]
dic= {'a':1, 'b': 2, 'c': 3}
testPoint(*lst)
testPoint(**dic)
testPoint(*lst, **dic)

print(bin(18))
print(oct(18))
print(hex(18))

print(sum([5, 7, 9, 11, 45, 23]))
'''
a= 18
print(format(a, '08b'))
b= '中'
c=ord(b)
print(c)
print(chr(c))

lst= ['a', 'b', 'c']
for index, value in enumerate(lst):
    print(index, value)