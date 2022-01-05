## python学习--day13
**内容概述**
- 标准库(STL)上
****
重点知识
- File
- SQLite
- Data/Time
- Random Values
- Emails
****

### Files
```text
    需要引入的库1： from pathlib import Path    # 路径相关的库
```
**查询性特征**
```python
from pathlib import Path


path = Path("package/subpackage/__init__.py")
print(path.name)           # 文件完整名
print(path.is_dir())       # 是否是文件夹
print(path.is_file())      # 是否是文件
print(path.stem)           # 文件名
print(path.suffix)         # 文件后缀
print(path.parent)         # 上层文件名
print(path.absolute())     # 绝对路径
'''
__init__.py
False
True
__init__
.py
package\subpackage
C:\Users\Gao\PycharmProjects\pythonProject\package\subpackage\__init__.py
'''

path1 = Path('./package')
path2 = path1.with_name('offer.txt')      # 将目录更改为当前目录下另一文件，若不存在则报错
print(path2.absolute())
'''
C:\Users\Gao\PycharmProjects\pythonProject\offer.txt
'''
```
**获取型特征**
```python
from pathlib import Path


path1 = Path('./package')
# path1.mkdir()      # 对该路径建立文件
# path1.rmdir()      # 删除
# path1.exists()     # 判断是否存在
# path1.rename()     # 重命名
# path1.iterdir()    # 获取当前目录的文件迭代器，可以用于遍历其下所有子文件
# path1.global('正则表达式')  # 匹配查找文件，返回生成器
# path1.rglob('正则表达式')   # 匹配查找文件，返回生成器
```
```python
# iterdir()的具体使用
# 第一种借助for循环，直接读取
path4 = Path('./package')
for p in path4.iterdir():
    print(p)


# 第二种借助生成器表达式，直接形成容器
filelst = [p for p in path4.iterdir() if path4.is_dir()]
print(filelst)

'''
[WindowsPath('package/subpackage'), 
 WindowsPath('package/__init__.py'), 
 WindowsPath('package/__pycache__')]
'''
```
**功能性特征**
```text
# 依据路径实现读写
    path2.read_text(encoding='utf-8')              # 读取路径下文件中的内容
    path2.write_text('欢迎加入', encoding='utf-8')  # 此时的写是直接覆盖原有的内容
    
# 依据路径进行文件复制
    src = Path('...')  # 源文件路径
    des = Path('...')  # 目标文件路径
    
    des.write_text(src.read_text('encoding='utf-8'), encoding='utf-8')  # 方式一
    
    import shutil
    shutil.copy(src, des)                     # 方式二，引入shutil库 
```

**操作ZIP文件**
```text
    引入头文件
    from zipfile import ZipFile
    最重要的功能————>解压
    with ZipFile(path) as zip:
        zip.extractall('test')     # 注意只能用于解压包格式
    '''
    几个坑：
        1.ZipFile所修饰的必须为非空的zip文件
        2.path.rmdir()函数所删除的必须是空文件
    '''
```

**CSV文件**
```text
    csv格式：
        采用逗号作为分割，在文本文件中建立的类似于表格信息的文件
```
```text
    import csv                  # 引入库csv
    # 写入csv
    with open(file_path, 'w', newline='') as file:   # 增加newline的key值可以保证行与行之间没有空行
        writer = csv.writer(file)         # 先设计为csv的writer
        writer.writerow(['id', 'num'])    # 按行写入
        writer.writerow([1, 5])
        writer.writerow([2, 6])
        
    
    # 读取csv
    with open(file_path, 'r') as file:
        reader = csv.reader
        print(list(reader))
    '''
    [['id', 'num'], ['1', '5'], ['2', '6']]        # 可以看到数字也被读取为str类型，使用时注意类型转换！！！
    '''
```
**JSON文件**
```text
    json格式：
        在python中的表现形式为[{}, {}, {}],经常用作前后端传输数据的格式
```
```python
    # 对json文件操作，既需要json库也需要Path库
import json
from pathlib import Path

# 对json文件写入
census_data = [
        {'id': 1, 'name': 'Allen', 'salary': 1000},
        {'id': 2, 'name': 'Bob', 'salary': 2000},
    ]
data = json.dumps(census_data)            # 转换格式
Path('./json_test.json').write_text(data)

# 对json文件读取
data = Path("./json_test.json").read_text()
movie = json.loads(data)                 # 转换格式
print(movie)
```

### SQLite
```text
   准备的工具 db browser for sqlite  非常好用类似于 navicat 数据库可视化工具
   导包 import sqlite3
```
```python
    
# 代码实例————> 插入数据

from pathlib import Path
import sqlite3

datas = json.loads(Path('./json_test.json').read_text()) 
with sqlite3.connect('db.sqlite3') as conn:                    # 连接数据库
    command = 'INSERT INTO FRIEND VALUES(?,?,?)'               # 设置指令
    for data in datas:                              
        conn.execute(command, tuple(data.values()))            # 插入数据
    conn.commit()                                              # 提交命令

# 代码实例————> 读取数据

import sqlite3
with sqlite3.connect('db.sqlite3') as conn:                    # 连接数据库
    command = 'SELECT * FROM FRIEND'               # 设置指令
    course = conn.execute(command)
    # print(list(course))                        # 方式一：[(1, 'Allen', 1000), (2, 'Bob', 2000)]
    for row in course:
        print(row)    
    # 方式二：
    # (1, 'Allen', 1000)
    # (2, 'Bob', 2000)
```

### Date&&Time
```text
Time模块
    import time
主要方法time.time() 用于返回当前时间——>两端时间差值计算运行时间
```
```python
start = time.time()
for i in range(1000000):
    pass
end = time.time()
ti = end - start
print(ti)   # 0.01894855499267578
```
```text
DateTime模块
    import datetime
使用方式：
    dt1 = datetime(2022, 1, 1)
    dt2 = datetime.now()
    dt3 = datetime.strptime('2022/1/1', '%Y/%m/%d')
    print(dt1, dt2, dt3)
    '''
    2022-01-01 00:00:00 2022-01-05 16:56:29.491072 2022-01-01 00:00:00
    '''
```
```python
# 引入timedelta，表达的内容更细致
from datetime import datetime, timedelta
print(datetime.now())
dt1 = datetime.now() + timedelta(days=1, seconds=60)
print(dt1)
print("days", dt1.day)
print('hours', dt1.hour)
print('minutes', dt1.minute)
print('seconds', dt1.second)
```

### random values
```text
导入模块：
    import random
主要功能;
    rand1 = random.random()
    rand2 = random.randint(0, 10)
    rand3 = random.choice([1, 2, 3, 4, 5])
    rand4 = random.choices([1, 2, 3, 4, 5], k=2)
    rand5 = ''.join(random.choices(string.digits+string.ascii_lowercase, k=4))
    print(rand1, '\n', rand2, '\n', rand3, '\n', rand4, '\n', rand5)
    '''
    0.09231490723726654 
     1 
     1
     [5, 5]
     2c12
    '''
```

### Browser && Email
**Browser**
```python
# 导入模块
import webbrowser

# 打开浏览器
webbrowser.open('https://www.baidu.com/')  # 会自动打开网站
```

**Email**
```python
# 导入模块
from email.mime.multipart import  MIMEMultipart        # 引入邮件对象
from email.mime.text import MIMEText                   # 引入内容对象
import smtplib                                         # 引入发送协议SMTP
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
```
```python
# 示例代码
message = MIMEMultipart()
message['from'] = 'Gao Haoyu'
message['to'] = '1315411340@qq.com'
message['subject'] = 'python_email'
message.attach(MIMEText('this is an email which is passed by python', 'plain'))
# 此处也可增加照片
message.attach(MIMEImage(Path('image_path').read_bytes()))          # 增加照片
# 增加HTML文件
template = Template(Path('./123.html').read_text())
body = template.substitute({'name': 'Bob'})        # 指定特殊内容, 采用字典的方式对应
message.attach(MIMEText(body, 'html'))

with smtplib.SMTP(host='smtp.qq.com', port=25) as smtp:    # qq邮箱需要额外的验证
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email_name', 'password')
    smtp.send_message(message)
    print('sent...')
```
123.html,其中$name为通配符
```html
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
hi, $name, this is test             
</body>
</html>
```