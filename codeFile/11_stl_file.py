import string
from pathlib import Path
from time import ctime
import shutil
from zipfile import ZipFile
import csv
import json
import sqlite3
import time
from datetime import datetime, timedelta
import random

path = Path("package/subpackage/__init__.py")
'''
print(path.name)           # 文件完整名
print(path.is_dir())       # 是否是文件夹
print(path.is_file())      # 是否是文件
print(path.stem)           # 文件名
print(path.suffix)         # 文件后缀
print(path.parent)         # 上层文件名
print(path.absolute())
'''

path1 = Path('./package')

'''
print(path1.absolute())
path2 = path1.parent
print(path2)
path2 = path1.with_name('offer.txt')
print(path2.absolute())

print(ctime(path2.stat().st_ctime))
print(path2.read_text(encoding='utf-8'))
path2.write_text('欢迎加入', encoding='utf-8')

print(path2.read_text(encoding='utf-8'))
path_tt = Path('./tt.txt/11.txt')
path_tt.write_text(path2.read_text(encoding='utf-8'), encoding='utf-8')
path_tt.write_text('')

shutil.copy(path2, path_tt)
'''

'''
print(path2.exists())
path4 = Path('./package')


filelst = [p for p in path4.iterdir() if path4.is_dir()]
print(filelst)
'''


def test01(path):
    return path.glob('*.py')

def test02(path):
    return path.rglob('*.md')

def test03(path):
    with ZipFile(path) as zip:
        print(zip)
        zip.extractall('test')


def test04():
    with open('./csv_test.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'num'])
        writer.writerow([1, 5])
        writer.writerow([2, 6])

    with open('./csv_test.csv', 'r') as file:
        reader = csv.reader(file)
        print(list(reader))


def test05():
    census_data = [
        {'id': 1, 'name': 'Allen', 'salary': 1000},
        {'id': 2, 'name': 'Bob', 'salary': 2000},
    ]
    data = json.dumps(census_data)
    Path('./json_test.json').write_text(data)


def test06():
    data = Path("./json_test.json").read_text()
    movie = json.loads(data)
    print(movie)


def test07():
    datas = json.loads(Path('./json_test.json').read_text())
    # print(datas)
    with sqlite3.connect('db.sqlite3') as conn:
        command = 'INSERT INTO FRIEND VALUES(?,?,?)'
        for data in datas:
            conn.execute(command, tuple(data.values()))
        conn.commit()


def test08():
    with sqlite3.connect('db.sqlite3') as conn:  # 连接数据库
        command = 'SELECT * FROM FRIEND'  # 设置指令
        course = conn.execute(command)
        # print(list(course))
        for row in course:
            print(row)


def test09():
    start = time.time()
    for i in range(1000000):
        pass
    end = time.time()
    ti = end - start
    print(ti)


def test10():
    dt1 = datetime(2022, 1, 1)
    dt2 = datetime.now()
    dt3 = datetime.strptime('2022/1/1', '%Y/%m/%d')
    print(dt1, dt2, dt3)


def test11():
    print(datetime.now())
    dt1 = datetime.now() + timedelta(days=1, seconds=60)
    print(dt1)
    print("days", dt1.day)
    print('hours', dt1.hour)
    print('minutes', dt1.minute)
    print('seconds', dt1.second)


def test12():
    rand1 = random.random()
    rand2 = random.randint(0, 10)
    rand3 = random.choice([1, 2, 3, 4, 5])
    rand4 = random.choices([1, 2, 3, 4, 5], k=2)
    rand5 = ''.join(random.choices(string.digits+string.ascii_lowercase, k=4))
    print(rand1, '\n', rand2, '\n', rand3, '\n', rand4, '\n', rand5)


import webbrowser
def test13():
    webbrowser.open('https://www.baidu.com/')



from email.mime.multipart import  MIMEMultipart        # 引入邮件对象
from email.mime.text import MIMEText                   # 引入内容对象
import smtplib                                         # 引入发送协议SMTP
from string import Template

def test14():
    message = MIMEMultipart()
    message['from'] = 'Gao Haoyu'
    message['to'] = '1315411340@qq.com'
    message['subject'] = 'python_email'
    message.attach(MIMEText('this is an email which is passed by python', 'plain'))

    template = Template(Path('./123.html').read_text())
    template.substitute({'name': 'Bob'})

    with smtplib.SMTP(host='smtp.qq.com', port=25) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('1315411340@qq.com', 'gao19970808abc')
        smtp.send_message(message)
        print('sent...')


import sys
def test15():
    if len(sys.argv) == 1:
        print('one argument')
    else:
        print('more than one')


import subprocess
def test16():
    ret = subprocess.run(['python', 'subprocess_test.py'], capture_output=True, text=True)
    print(ret.args)
    print(ret.stdout)
    print(ret.returncode)
'''
for p in test02(path1):
    print(p)

path_zip = Path('./package/zip_test.zip')
# test03(path_zip)
Path('./test').rmdir()
'''
# test04()
# test05()
# test06()
# test07()
# test08()
# test09()
# test10()
# test11()
# test12()
# test13()
# test14()
# test15()
# test16()
open('./123.html')
