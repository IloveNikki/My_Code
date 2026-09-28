# 生成随机漫步
# import matplotlib.pyplot as plt
# from RandomWalk import RandomWalk
# rw=RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_values,rw.y_values,s=15,c='red')
# plt.show()

# 给你生成的散点图加上渐变映射
# import matplotlib.pyplot as plt
# from RandomWalk import RandomWalk
# while True:
#     rw=RandomWalk()
#     rw.fill_walk()
#     point_numbers=list(range(rw.num_points))
#     plt.scatter(rw.x_values,rw.y_values,c=point_numbers,s=15,cmap=plt.cm.Greens)
#     plt.show()
#
#     keep_running=input("Make another walking?(y/n)")
#     if keep_running=='y':
#         break

# 重新绘制起点和终点
#
# import matplotlib.pyplot as plt
# from RandomWalk import RandomWalk
#
# while True:
#     rw=RandomWalk()
#     rw.fill_walk()
#     point_numbers=list(range(rw.num_points))
#     plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='None',s=15)
#
#     plt.scatter(0,0,c='green',edgecolors='None',s=100)
#     plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='None',s=100)
#     '''注意【-1】！！！'''
#     ax=plt.gca()
#
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
#     plt.show()
#
#

# 隐藏坐标轴
#
# import matplotlib.pyplot as plt
# from RandomWalk import RandomWalk
#
# while True:
#     rw=RandomWalk()
#     rw.fill_walk()
#     point_numbers=list(range(rw.num_points))
#     plt.scatter(rw.x_values,rw.y_values,s=15,edgecolors='None',cmap=plt.cm.Blues,c=point_numbers)
#     plt.scatter(0,0,c='green',edgecolors='None',s=100)
#     plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='None', s=100)
#     ax=plt.gca()
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
#     plt.show()
#
#     plt.show()


# 创建点数
# import matplotlib.pyplot as plt
# from RandomWalk import RandomWalk

# while True:
#     rw=RandomWalk(50000)
#     rw.fill_walk()
#     point_numbers=list(range(rw.num_points))
#     plt.scatter(rw.x_values,rw.y_values,c=point_numbers,edgecolors='None',s=1)
#     plt.savefig('漫步图.png')

调整尺寸
import matplotlib.pyplot as plt
from RandomWalk import RandomWalk
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.figure(figsize=[6,8])
    plt.scatter(rw.x_values,rw.y_values,c='green',edgecolors='none',s=10)
    plt.show()

