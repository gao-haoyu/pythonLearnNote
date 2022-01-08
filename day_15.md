## python学习--day15
**内容概述**
- important python package
****
重点知识
- numpy
- pandas
****

### 1.numpy  ————> pip install numpy
**基础操作**
```python
# pip install numpy  安装numpy
import numpy as np

array = np.array([[1,2,3],[4,5,6]])      # numpy 中 array
print(array)
print(array.shape)                       # 打印array的shape 2*3的矩阵

array = np.zeros((3,4))                  # 采用zero初始化一个3*4的矩阵
print(array)                             # 此时默认为float类型
array = np.zeros((3,4), dtype= int)      # 指定数据类型
print(array)
# 初始化数组的别的用法
array_one = np.ones((3,4), dtype= int)
array_full = np.full((3,4), 5)
array_random = np.random.random((3,4))
print(array_one)
print(array_full)
print(array_random)
# 索引&提取元素
print(array_random[0,0])                # array的索引形式[m,n]
print('=======================================')
print(array_random>0.1)                 # 判断是否符合条件输出逻辑值矩阵
print('=======================================')
print(array_random[array_random>0.1])   # 将满足条件的值单独输出
print('=======================================')
print(np.sum(array_one))                # 计算矩阵和
print('=======================================')
print('=======================================')
print(np.floor(array_random))                        # 向下取整
print('=======================================')
print(np.ceil(array_random))                         # 向上取整
print('=======================================')
print(np.round(array_random))                        # 四舍五入
print('=======================================')
print(array_one+array_full)                          # array之间加减
print('=======================================')
print(array_full-array_one)             # array也支持直接的数据操作，比如array*2.5表示所有元素*2.5
```
```python
'''
[[1 2 3]
 [4 5 6]]
(2, 3)
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
[[1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]]
[[5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]]
[[0.00539246 0.16124944 0.58443613 0.96413424]
 [0.21095589 0.55576921 0.56698598 0.4114695 ]
 [0.16837521 0.53846997 0.47877116 0.76997063]]
0.005392464014834286
=======================================
[[False  True  True  True]
 [ True  True  True  True]
 [ True  True  True  True]]
=======================================
[0.16124944 0.58443613 0.96413424 0.21095589 0.55576921 0.56698598
 0.4114695  0.16837521 0.53846997 0.47877116 0.76997063]
=======================================
12
=======================================
=======================================
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
=======================================
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
=======================================
[[0. 0. 1. 1.]
 [0. 1. 1. 0.]
 [0. 1. 0. 1.]]
=======================================
[[6 6 6 6]
 [6 6 6 6]
 [6 6 6 6]]
=======================================
[[4 4 4 4]
 [4 4 4 4]
 [4 4 4 4]]
'''
```
```python
# 矩阵的乘法
# type1：逐个相乘  matrix1*matrix2
# type2: 矩阵法则 np.dot(matrix1, matrix2)
array_one = np.array([1,2,3])
array_two = np.array([4,5,6])
array_vermerge = np.vstack((array_one, array_two))   # 上下方向合并
print('=================array_vermerge')
print(array_vermerge)
array_vermerge1 = np.vstack((array_two, array_one))
print('=================array_vermerge1')
print(array_vermerge1)
print('=================reshape')
print(array_vermerge1.reshape((3,2)))
print('=================逐个相乘')
print(array_vermerge*array_vermerge1)
print('=================dot')
print(np.dot(array_vermerge, array_vermerge1.reshape((3,2))))
```
```python
'''
=================array_vermerge
[[1 2 3]
 [4 5 6]]
=================array_vermerge1
[[4 5 6]
 [1 2 3]]
=================reshape
[[4 5]
 [6 1]
 [2 3]]
=================逐个相乘
[[ 4 10 18]
 [ 4 10 18]]
=================dot, 2*3*3*2
[[22 16]
 [58 43]]
'''
```

**Array的合并与分割**
```python
# Array的合并
array_one = np.array([1, 2, 3])
array_two = np.array([4, 5, 6])
array_vermerge = np.vstack((array_one, array_two))  # 上下方向合并
print('=================上下合并结果')
print(array_vermerge)

array_hormerge = np.hstack((array_one, array_two))  # 左右方向合并
print('=================左右合并结果')
print(array_hormerge)

'''
=================上下合并结果
[[1 2 3]
 [4 5 6]]
=================左右合并结果
[1 2 3 4 5 6]
'''

# Array的分割
array = np.arange(12).reshape((3,4))
print('=================初始矩阵')
print(array)
print('=================按行分割')
print(np.split(array, 3, axis=0))
print('=================按列分割')
print(np.split(array, 2, axis=1))

'''
=================初始矩阵
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
=================按行分割
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
=================按列分割
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
'''
```
### 2.pandas
**pandas库应用广，内容偏多，参考官方资料，后续结合案例来应用.**
#### [pandas官方资料](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
