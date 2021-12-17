## python学习--day02
**内容概述**
- 基本数据类型，int, float, bool
- 字符串str
****
重点函数：upper, split, replace, strip, isdigit
****
### int/float/bool
    int——>对应基础运算，没有特别之处
    float——>注意其误差的存在，如print(10/3)可能会得到3.33333335
    bool——>注意其类型的转换
           非零数均是True，0为False
           非空字符串均是True，空字符串为False
            a= bool("")
            b= bool(" ")
            print(a)     #False
            print(b)     #True

### 字符串
#### 1.字符串的格式化
    所谓字符的格式化，意味着形成字符的某一模板，可以向一段固定的子符串中插入不同的数据来动态构成字符串
基本方式有四种 
```python
name= input('请输入名字:')
age= int(input('请输入年龄'))
s1= '我叫%s, 今年%d岁' % (name, age)
s2= '我叫{}, 今年{}岁'.format(name, age)
s3= f'我叫{name}, 今年{age}岁'      #推荐用这种
print(s1)
print(s2)
print(s3)

'''
请输入名字:Hermit 
请输入年龄24
我叫Hermit, 今年24岁
我叫Hermit, 今年24岁
我叫Hermit, 今年24岁
'''
```
 
#### 2.索引和切片
- 索引，拿取字符串中某一特定位
- 切片，拿取字符串中某一段数据
```python
#语法
#s= str[postion]  注：从0开始计数
#s= str[start:end]  注：左闭右开[start, end)
```
```python
#代码示例
ss= 'you are best'
print(ss[5])
print(ss[-1])    #取倒数的数据
print(ss[0:6])   
print(ss[: 0])   #从0开始可以省略
print(ss[6: ])   #结尾也可以省略
'''
r
t
you ar
you ar
e best
'''
```
**关于切片的高级用法**
```python
#切片的完整参数表为：ss= str[start:end:step]   step默认为1
#当希望切片从右向左读取时，将start、end、step设为负的
#step不为1时，意味着步长内数据段拿取一个，若step为正，提取左侧，step为负，提取右侧
```
```python
#代码示例1
ss= 'you are best'
print(ss[::-1])     #其结果为，tseb era uoy
print(ss[1:6:3])    #其结果为，oa
print(ss[-1:-6:-3]) #其结果为，tb
```

#### 3.字符串的常规操作
- 大小写转换
```python
ss= 'i have dream'
s1= ss.upper()          #转为全大写，最最重要的函数
s2= s1.lower()          #转为全小写
s3= s2.title()          #单词开头大写
```

```python
#操作实例
ss= 'i have dream'
s1= ss.upper()          #转为全大写，最最重要的函数
s2= s1.lower()          #转为全小写
s3= s2.title()          #单词开头大写
print(s1+'-'+s2+'-'+s3)
print(ss)               #不影响字符串本身

'''
I HAVE DREAM-i have dream-I Have Dream
i have dream
'''
```

- 剪切&替换(三个函数都比较重要)
```python
ss= '  i have a dream   '
s1= ss.strip()              #去除头尾空格
s2= s1.replace(" ", "")     #将所有空格替换掉
s3= s1.split(" ")           #用空格切割字符串，并用列表存储
```

```python
#代码实例
ss= '   i have a dream    '
print(ss.strip())
print(ss.replace(" ",""))
print(ss.split(" "))
'''
i have a dream
ihaveadream
['', '', '', 'i', 'have', 'a', 'dream', '', '', '', '']
'''
```

- 查找和判断
```python
#查找操作
ss.find('abc')        #查找abc在不在ss之中，查到返回位置，查不到返回-1
ss.index('abc')       #查找abc在不在ss之中，查到返回位置，查不到报错
'abc' in ss           #查到返回True，查不到返回False

#判断操作
ss.startswith('a')    #判断以a开头
ss.endswith('a')      #判断以a结尾
ss.isdigit()          #判断是不是整数
ss.isdecimal()        #判断是不是小数
```
```python
#代码示例
s1= input("请输入：")
print(s1.isdigit())
print(s1.startswith('1'))
print(s1.endswith('2'))
'''
请输入：123
True
True
False
'''
```

- 字符串操作补充
```python
#len函数
len(ss)   #输出字符串长度
#join函数
ss.join(list) #与split作用刚好相反，采用ss将list中的个元素拼接一起
```
```python
#代码示例
ss= 'ni_hao_world'
print(len(ss))
ls= ss.split("_")
print(ls)
print("+".join(ls))

'''
12
['ni', 'hao', 'world']
ni+hao+world
'''
```