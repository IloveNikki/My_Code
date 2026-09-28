import numpy as np
stocks=np.random.normal(loc=0,scale=1,size=(8,10))
print(stocks)

n=stocks[0,0:3]
# 第一个股票的前三个数据 从0开始数
print(n)
al=np.array([
    [[1,2,3],[4,5,6]],[[12,23,7],[7,8,9]]
             ])
print(al.shape)
# 索引
print(al[0,1,0])
# 直接改值
al[0,1,0]=100
print(al)
#           1形状修改  返回新的数据原始数据没改
h=stocks.reshape(10,8)
print(h)
# resizeshape 没有返回值 对原始的ndarray 进行了修改
print(stocks.resize(10,8))
print(h.shape)
print(stocks.shape)
# 可以再改回来
print(stocks.resize(8,10))
print(stocks.shape)
# print(stocks)

# 数组的转置  完全变 行变列 列变行
print(stocks.T)



#      类型修改
print(stocks.dtype)
# 把浮点改为其他类型
print(stocks.astype("int32"))


# print(stocks.tobypes())


# 数组的去重
temp=np.array([[1,2,3,4],[3,4,5,6]])
print(temp)
print(np.unique(temp))
# 拍扁成一维度的
print(temp.flatten())
q=temp.flatten()
# 降维成集合的形式
print(set(q))


# ndarray的运算
# 1逻辑运算
print(stocks>0.5)
# 统一操作某一条件的数据
print(stocks[stocks>0.5])
# np.all 全真即为真 一否则全否 &&
# np.any 全否即为否 一真则全真 ||
print(stocks[0:2,0:5])
y=stocks[0:2,0:5]
print(y>0)
# 是否全是上涨的
print(np.all(y>0))
# 是否有上涨的
print(np.any(y>0))

# 三元运算符
m=stocks[:4,:4]
print(m)
# 正为1 负为0
print(np.where(m>0,1,0))
print(np.where((m>0.5)&(m<1),1,0))
print(np.where((m>0.5)|(m<-0.5),1,0))


# 2统计运算
print(m.max())
print(np.max(m))
# 按列求最大值
print(m.max(axis=0))
# 按行求最大值(1和-1都是一个意思
print(np.max(m,axis=1))
print(np.max(m,axis=-1))

# 返回最大值和最小值所在的位置
# 按列
print(m.argmax(axis=0))
# 按行
print(np.argmax(m,axis=1))
# max min 等等


# 3数组减运算

sum=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(sum)
# 数组与数
# 所有元素都加1 可加可减可乘可除
print(sum+1)
# 反而对于原生没有引用numpy的python数组来说 会报错
a=[1,2,3,4,5,6]
# print(a+1)
print(a*2)
# 是把该数组重复写2遍

# 数组与数组
# 不同形式的数组运算要满足广播机制



# 广播机制 数组与数组

# 矩阵运算 m*n    n*l  合并之后是m*l


# 合并拼接
# 水平
# 普通的
h=np.array((1,2,3))
print(h.shape)
f=np.array((2,3,4))
print(np.hstack((h,f)))
# 拼接在一起了（水平
h=np.array(([1],[2],[3]))
f=np.array(([2],[3],[4]))
print(np.hstack((h,f)))
# 竖直
h=np.array(([1],[2],[3]))
f=np.array(([2],[3],[4]))
print(np.vstack((h,f)))

# concatenate()  即可进行水平拼接也可以是竖直拼接
s=np.array([[1,2],[3,4]])
l=np.array([[5,6]])
# SHUIPING
print(np.concatenate((s,l.T),axis=1))
# SHIZHI
print(np.concatenate((s,l),axis=0))

# 分割


# 读取。csv文件 读取出缺失值会得出nan

#   有缺失值 1 直接删除2 数据量少  求平均值放进去
# 缺失值就是 读取到的问你安慰float时，如有缺失值（none),就会出现nan

# numpy 处理比pabnas差
# 运算比pandas好
