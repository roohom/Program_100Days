# DATA ANALYSIS

>约定：
>
>Python社区对一些常用模块采用了命名约定
>
>~~~~python
>import numpy as np
>import matplotlib.pylot as plt
>import pandas as pd
>~~~~



## 1.NumPy基础：数组与向量化计算

### 1.1Numpy ndarray:多维数组对象

ndarray是Python中的一个快速、灵活的大型数据集容器。数组允许你使用类似于标量的操作语法在整块数据上进行数学计算。

每一个数组都有一个shape属性，用以表征数组每一维度的数量；每一个数组都有一个dtype属性，用来描述数组的数据类型：

~~~~jupyter
In []:data.shape
Out[]:(2,3)

In []:data.dtype
Out[]:dtype('float64')
~~~~

#### 1.1.1 生成ndarray

使用array可以简单地生成数组。array函数可以接收任意的序列型数组，生成一个新的包含传递数据的NumPy数组。

~~~~jupyter
In []:data1 = [6, 7.5, 8, 0, 1]
In []:arr1 = np.array(data1)
In []:arr1
Out[]:array([6, 7.5, 8, 0, 1])
~~~~

使用ndim和shape属性可以检查数组的维度：

~~~~jupyter
In []:arr2.ndim
Out[]:2

In []:arr2.shape
Out[]:(2,4)
~~~~

除了np.array，还有其他方法可以生成新数组。zeros可以一次性生成全0数组，ones可以一次性生成全1数组。empty可以创建一个没有初始化数值的数组。

arange是Python内建函数range的数组版：

~~~~jupyter
In []:np.arange(15)
Out[]:array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
~~~~

