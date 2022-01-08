'''
ss= '123'
it= iter(ss)

print(next(it))
print(next(it))
print(next(it))

it= ss.__iter__()
print(it.__next__())
print(next(it))
print(it.__next__())

def func():
    print(1)
    yield 2
    print(3)
    yield 4

it= func()   #此时已经成为了一个生成器
print(it.__next__())
print(it.__next__())

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

#task1: 生成一个0-9的列表
lst= [i for i in range(10)]
print(lst)

#task2: 生成1、3、5、7、9列表
lst= [i for i in range(10) if i%2 == 1]
print(lst)

#task3: 生成字符串列表
lst= [f'数据{i}' for i in range(10)]
print(lst)

st= {i for i in range(10)}
print(st)

lst1= ['aa', 'bb', 'cc', 'dd']
lst2= [it.upper() for it in lst1]
print(lst2)


lst= ['aa', 'bb', 'cc', 'dd']
dic= {i:lst[i] for i in range(len(lst))}
print(dic)

gen= (i for i in range(5))
print(gen.__next__(), end=' ')
print(gen.__next__(), end=' ')
print(gen.__next__(), end=' ')
print(gen.__next__(), end=' ')
print(gen.__next__(), end=' ')

gen= (i for i in range(5))
for it in gen:
    print(it, end=' ')


gen= (i for i in range(5))
lst= list(gen)
print(lst)


fn= lambda a, b: a+b
print(fn(2,3))

lst1= ['Allen', 'Bob', 'Cindy']
lst2= ['一年级','二年级','二年级']
lst3= [6, 7, 7]
rest= zip(lst1, lst2, lst3)
rest= list(rest)
print(rest)


lst=['明', '张三', '李二狗', '王四麻子']
lst= sorted(lst, key= lambda a: len(a), reverse= True)
print(lst)


lst= [
    {'name': 'Allen', 'age': 18, 'salary': 100},
    {'name': 'Bob', 'age': 20, 'salary': 600},
    {'name': 'Cindy', 'age': 19, 'salary': 200},
    {'name': 'David', 'age': 22, 'salary': 500}
]
lst= sorted(lst, key= lambda dic: dic['age'])
print(lst)

lst2= sorted(lst, key= lambda dic: dic['salary'])       #依据薪水排序
print(lst2)

lst= [
    {'name': 'Allen', 'age': 18, 'salary': 100},
    {'name': 'Bob', 'age': 20, 'salary': 600},
    {'name': 'Cindy', 'age': 19, 'salary': 200},
    {'name': 'David', 'age': 22, 'salary': 500}
]
lst1= list(filter(lambda dic: dic['salary']> 300 , lst))
print(lst1)
'''
lst= [1, 2, 3, 4, 5]

lst1= list(map(lambda x: x*x , lst))
print(lst1)