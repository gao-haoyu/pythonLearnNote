## python学习--day14
**内容概述**
- popular python package
****
重点知识
- pip
- Web Scraping
- Browser Automation
- PDFs
- Excel Spreadsheets
****

### 1.pip
```text
主要功能：
    是实现package的安装(install)，卸载(uninstall)
```
```shell
# 以requests包为例解释一些操作
>>pip install request           # 安装最新版本request
>>pip install request==2.9.0    # 安装2.9.0的版本
>>pip install request==2.9.*    # 安装2.9下的最新子版本
>>pip install request~=2.9.0    # 安装支持2.9.0的最新版本
>>pip uninstall request         # 卸载
```
```python
import requests # 安装之后，便可以当作常规的文件调用

ret = requests.get('https://www.baidu.com/')
print(ret)                                    # <Response [200]>
```

### 2.关于配置文件&信息隐藏
```text
总体思路：
   在配置文件config.py中放置重要的信息数据，之后通过import的方式调用到正确位置
   设置.gitignore文件，在文件中记录需要隐藏的文件的文件名
```

### 3.web scripting  ————> pip install beautifulsoup4
```text
目的：
    从网页中的HTML文件中，得到需要的信息
导入的package：
    beautifulsoup4
```
```python
import requests
from bs4 import BeautifulSoup


url = 'https://stackoverflow.com/questions'
repose = requests.get(url)

soup = BeautifulSoup(repose.text, 'html.parser')
questions = soup.select('.question-summary')
for question in questions :
    print(question.select_one('.question-hyperlink').getText())
    print(question.select_one('.vote-count-post').getText())
```
**这个select的用法，就是去观察HTML的标签中有哪些，依据标签直接提取内容**


### 4.Browser Automation  ————> pip install selenium
```text
目的：
    自动登录网页
package:
    selenium  && 还需要安装对应浏览器的驱动，参考https://pypi.org/project/selenium/
```
```python
from selenium import webdriver


browser = webdriver.Chrome()
# step1 : open webpage
url = 'https://github.com'
global browser
browser.get(url)
sign_up = browser.find_element_by_link_text('Sign up')       # 依据text获取element
sign_up.click()
sign_in = browser.find_element_by_link_text('Sign in →')
sign_in.click()

# step2 : enter message
username_box = browser.find_element_by_id('login_field')     # 依据id获取element
username_box.send_keys('******')                             # 键入文本的方式
password_box = browser.find_element_by_id('password')
password_box.send_keys('*******')
password_box.submit()

# step3 : quit webpage
assert 'gao-haoyu' in browser.page_source
browser.quit()
```

### 5.About PDF     ————> pip install pypdf2
```text
目的：
    python处理PDF文件
package：
    pypdf2
```
```python
import PyPDF2
with open('first.pdf', 'wb') as file:
    with open('./C语言C++常见面试题（含答案）.pdf', 'rb') as source:
        reader = PyPDF2.PdfFileReader(source)
        page = reader.getPage(0)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        writer.write(file)
```
```text
需要注意的点：
    1.打开文件采用二进制 'rb' 'wb'方式
    2.专门的reader和writer作为中间的媒介
    3.合并pdf，暂时出现一些问题，后续处理
```

### 6.Excel Spreadsheets ————> pip install openpyxl
```python
# example
wb = openpyxl.load_workbook('111.xlsx')     # 导入excel
print(wb.sheetnames)
sheet1 = wb['Sheet1']                       # 以字典形式拿到数据
print(sheet1.max_row)
print(sheet1.max_column)
sheet1.append([10, 11, 12])                 # 增加内容，也可insert插入数据
for row in range(1, sheet1.max_row + 1):    # 遍历一个表格中的数据
    for col in range(1, sheet1.max_column + 1):
        print(sheet1.cell(row, col).value)
wb.save('222.xlsx')                         # 保存文件
```
