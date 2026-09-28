# import matplotlib.pyplot as plt
#
# squares = [1, 4, 9, 16, 25]
# plt.plot(squares,linewidth=3)
# plt.title ("Square Numbers")
# plt.xlabel ("Value",fontsize=14)
# plt.ylabel ("Square",fontsize=14)
# plt.tick_params(axis='both',labelrotation=14)
# plt.show()


# import  matplotlib.pyplot as plt
# squares=[1,4,9,16,25]
# plt.plot(squares)
# plt.title('Square Numbers')
# plt.xlabel('Value')
# plt.ylabel('Square of Value')
# plt.tick_params(axis='both',labelsize=14)
# plt.show()

# 加上输入值会更好一些 就是改变默认值
# import matplotlib.pyplot as plt
# input_values=[1,2,3,4,5]
# squares=[1,4,9,16,25]
# plt.plot(input_values,squares,linewidth=5)
# plt.title('Number Images')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.tick_params(axis='both', which='major', labelsize=20)
# plt.show()


# 绘制一个点
# import matplotlib.pyplot  as plt
# plt.scatter(2,4,s=200)
# plt.title('Square numbers',fontsize=24)
# plt.xlabel('values',fontsize=14)
# plt.ylabel('y values',fontsize=14)
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.show()

# 绘制一个散点图
# import matplotlib.pyplot as plt
# x_values=list(range(1,1001))
# y_values=[x**2 for x in x_values]
# plt.scatter(x_values,y_values,c='red',edgecolor='none',s=40)
# plt.title('Title')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.axis([0,1100,0,1100000])
# plt.show()
#


# c是改变颜色的量（0，0，0）括号内分别控制红绿蓝
# import matplotlib.pyplot as plt
# x_values=list(range(1,1001))
# y_values=[x**2 for x in x_values]
# plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolor='none',s=40)
# plt.title('Title')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.axis([0,1100,0,1100000])
# plt.show()

# 散点图实现颜色映射
import matplotlib.pyplot as plt
x_values=list(range(1,1001))
y_values=[x**2 for x  in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)
plt.title('title')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.axis([0,1100,0,1100000])
plt.show()

#
# import scipy
# print(scipy.__version__)



# 各种库函数的使用
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats
#
# # 1. 生成一些随机数据 (使用 numpy)
# data = np.random.normal(loc=0, scale=1, size=1000)
#
# # 2. 使用 scipy 进行简单的统计计算 (比如核密度估计)
# kde = stats.gaussian_kde(data)
# x_range = np.linspace(-4, 4, 200)
#
# # 3. 开始绘图 (使用 matplotlib)
# plt.figure(figsize=(10, 6))
#
# # 画直方图
# plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Histogram')
#
# # 画 scipy 计算出的平滑曲线
# plt.plot(x_range, kde(x_range), 'r-', linewidth=2, label='KDE (Scipy)')
#
# plt.title('Data Visualization with Scipy & Matplotlib')
# plt.xlabel('Value')
# plt.ylabel('Density')
# plt.legend()
# plt.grid(True, linestyle='--', alpha=0.7)
#
# # 显示图表
# plt.show()
