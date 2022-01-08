# pip install numpy  安装numpy
import numpy as np
def test01():
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
    print(array_one+array_full)
    print('=======================================')
    print(array_full-array_one)

def test02():
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
    array_hormerge = np.hstack((array_one, array_two))   # 左右方向合并
    # print(array_hormerge)

def test03():
    array = np.arange(12).reshape((3,4))
    print('=================初始矩阵')
    print(array)
    print('=================按行分割')
    print(np.split(array, 3, axis=0))
    print('=================按列分割')
    print(np.split(array, 2, axis=1))

def test04():
    array_one = np.array([1, 2, 3])
    array_two = np.array([4, 5, 6])
    array_vermerge = np.vstack((array_one, array_two))  # 上下方向合并
    print('=================上下合并结果')
    print(array_vermerge)

    array_hormerge = np.hstack((array_one, array_two))  # 左右方向合并
    print('=================左右合并结果')
    print(array_hormerge)

test04()
