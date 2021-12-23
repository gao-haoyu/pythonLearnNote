
## python学习--day05
**内容概述**
- 文件操作
****
重点知识  
- 文件的读取
- 文件的写入
- 文件的修改
    ```text
    1.绝对路径&相对路径
    2.打开方式
    r: 读取文本
    w: 写入文本，每次都会打开一个空白
    a: 追加文本，在原有文件上新增
    rb:读取非文本，无需encoding
    wb:写入非文本，无需encoding
    with的写法，换行的写法\
    3.文件的修改：借助os删除&重命名
    ```
****

### 1.文件的读取
```text
基本格式：
变量= open(文件名, mode= '打开方式', encoding= '编码方式')
变量.read() 得到文件内容
变量.close()
见详细代码示例1

需要注意的点：文件的绝对路径&相对路径
1.绝对路径：从根目录开始写上完整路径
2.相对路径：./当前目录，  ../上一层目录
```
```text
文件读取方式：
1.read()  全部读取
2.readline() 一行一行的读取
3.readlines() 多行读取，且用列表存储
4.采用for循环读取，这种方式最为重要
见代码示例2
```

```python
#示例1
f = open("offer.txt", mode= 'r', encoding='UTF-8')
context= f.read()                            #方式1
print(context)
'''
恭喜您被公司录用，欢迎您的加入。
'''
```
```python
#示例2
'''
offer.txt
恭喜您被公司录用，欢迎您的加入。
您的岗位为：xxx
目标薪酬为：xxx
'''
#逐行读取
f = open("offer.txt", mode= 'r', encoding='UTF-8')
cont= f.readline().strip()    #若不加strip()，会有额外的空行
print(cont)
cont= f.readline().strip()        #方式2
print(cont)
cont= f.readline().strip()
print(cont)
'''
恭喜您被公司录用，欢迎您的加入。
您的岗位为：xxx
目标薪酬为：xxx
'''

#多行读取
f = open("offer.txt", mode= 'r', encoding='UTF-8')   
cc= f.readlines()                #方式3
print(cc)
'''
['恭喜您被公司录用，欢迎您的加入。\n', '您的岗位为：xxx\n', '目标薪酬为：xxx']
'''

#for循环读取
for line in f:                   #方式4
    print(line.strip())
'''
恭喜您被公司录用，欢迎您的加入。
您的岗位为：xxx
目标薪酬为：xxx
'''
```

### 2.文件的写入
```text
文件写入基本方式
f= open("文件名", mode= 'w', encoding= 'utf-8')   
f.write('context')
#w模式下打开，若文件本身不存在，自动添加。
#w模式下，每次打开都会将之前的内容清空。

f= open('文件名', mode= 'a', encoding= 'utf-8')
f.write('context')
#a模式下打开，向文件中追加内容
#见示例代码3
```
```python
#示例3
#需求，将列表中的数据写入到文件中
lst= ['Amy','Bob', 'Cindy']
f= open('name.txt', mode= 'w', encoding='utf-8')
for nam in lst:
    f.write(nam)
    f.write('\n')
f.close()
'''
#name.txt
Amy
Bob
Cindy

'''

#再追加一个David
f= open('name.txt', mode= 'a', encoding='utf-8')
f.write('David')
f.write('\n')
f.close()
'''
#name.txt
Amy
Bob
Cindy
David

'''
```

### 3.最为常用的文件读写方式——with
```text
#语法示例
with open('filename', mode= 'model', encoding= 'utf-8') as f:
    #执行对文件的操作，后续不需要自己close文件，会自动关闭。
```
```python
#示例4
with open('name.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
'''
Amy
Bob
Cindy
David
'''
```

### 4.非文本文件的处理&文件的复制
```text
注意点：非文本文件，没有encoding，其打开格式要标注b，表明是非文本。
with open('test.jpg', mode= 'rb') as f：
    for line in f:
        print(line)
'''
打印出的内容为byte形式
'''
```
```python
#示例5
#图片文件的复制：将test文件，复制出一份副本test2
with open('test.jpg', mode= 'rb') as f, open('test2.jpg',mode= 'wb') as f2:
    for line in f:
        f2.write(line)

#上述的代码也可写出如下的格式：   可读性更好
with open('test.jpg', mode= 'rb') as f, \
        open('test2.jpg',mode= 'wb') as f2:
    for line in f:
        f2.write(line)
```

### 5.文件的修改——>文件的删除&重命名
```text
应用场景：
'''
#name.txt
王一
王二
王三
张四
张五
张六
'''
需求:将name.txt中的王姓均改为张姓
思路：先将修改后的内容重新赋值给一个文件，之后删除源文件，再重命名新文件。实现修改的效果。
```

```python
import os

with open('name.txt', mode='r', encoding='utf-8') as f1,\
        open('name1.txt', mode='w', encoding='utf-8') as f2:
    for line in f1:
        line = line.strip()  # 去除换行符
        if line.startswith('王'):
            line = line.replace('王', '张')     #replace之后注意保存新的字符
        f2.write(line)
        f2.write('\n')       # 添加换行符

os.remove('name.txt')                        #文件的删除
os.rename('name1.txt', 'name.txt')           #文件重命名

'''
张一
张二
张三
张四
张五
张六

'''
```