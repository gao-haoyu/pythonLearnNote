#dic = {'Amy': 90, 'Bob': 93, 'Cindy': 88}
#print(dic['Bob'])
'''
name= input('Please enter your name: ')
score= dic.get(name)
if score is None:
    print('Not exist')
else:
    print(score)


for item in dic.items():
    print(item)
    print(type(item))
'''
'''
dic= {
    "teacherA":{'name': 'Henry',
              'students':{'AA': 85, 'BB': 88}},
    'teacherB':{'name': 'Harris',
              'students':{'CC': 86, 'DD': 87}},
}
print(dic['teacherA']['name'])
print(dic['teacherB']['students']['CC'])
'''
dic= {'AA': 15, 'BB': 60, 'CC': 85, 'DD': 23}
lst = list()
for k, v in dic.items():
    if v< 60:
        lst.append(k)
for name in lst:
    dic.pop(name)
print(dic)