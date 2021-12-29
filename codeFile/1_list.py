'''
aList= [1,2,3, "abc", 'a',['b', 'c']]
#for c in aList:
#   print(c)
print(f'长度为{len(aList)}')
print(aList[3])   #打印abc
print(aList[0:3])
print(aList[::3])
print(aList[::-1])
____________________________________________
'''
'''
lst= ['a', 'b', 'c']
#append:追加元素
lst.append('d')
print(lst)

#insert:插入元素
lst.insert(0, '0')
print(lst)

#extend:合并两个列表
subLst= ['e', 'f']
lst.extend(subLst)
print(lst)

ret= lst.pop(0)
print(lst)
print(ret)
______________________________
'''
'''
#代码示例
lst= [1, 2, 3]
#pop:弹出某一位置的元素，参数为index,返回弹出的元素
ret= lst.pop(2)
print(lst)
print(ret)
#

#remove:移除某一个元素，参数为data，不返回
lst.remove(2)
print(lst)
______________________________
'''
'''
lst= [1, 2, 3]
print(lst)
lst[0]= 0
ret= lst[0]
print(ret)
_________________
'''
'''
#方案一：只在循环体里修改&打印
def func(lst):
    for name in lst:
        if(name.startswith("张")):
            name= name.replace("张", "王")
        print(name)

#方案二：彻底的修改
def func2(lst):
    for i in range(len(lst)):
        name= lst[i]
        if(name.startswith("张")):
            newName= "王"+name[1:]
            lst[i]= newName

lst= ['张三','张四','张五','王一','王二','王六']

func(lst)
print(lst)

func2(lst)
print(lst)
'''
lst= [11, 12, 5 ,6 ,3]
lst.sort()
print(lst)
lst.sort(reverse= True)
print(lst)

lst1= [1,'a',['b',['c']]]
ret= lst1[2][1][0]
print(ret)

lst2= [1,2,2,3,4,5]
census= []
for it in lst2:
    if it == 2:
        census.append(it)

for it in census:
    lst2.remove(it)
print(lst2)
