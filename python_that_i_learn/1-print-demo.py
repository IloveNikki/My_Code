print("你好" + " 这是一句代码" + "哈哈")

print("Let\'s go")

print("\n")
print("我是第一行\n我是第二行")

print("""《静夜思》

床前明月光，疑是地上霜。
举头望明月，低头思故乡。""")


greet="您好，吃了么"
greet_chinese=greet
greet_english="Yo what's up,"
greet=greet_english
print(greet+"张山")
print(greet+"李古")
print(greet_chinese+"张山")

import math
result=math.sin(1)
print(result)

a=-1
b=-2
c=3
print((-b+(b**2-4*a*c)**(1/2))/(2*a))
print((-b-(b**2-4*a*c)**(1/2))/(2*a))

import math
a=-1
b=1
c=2
print((-b+math.sqrt(b**2-4*a*c))/(2*a))
print((-b-math.sqrt(b**2-4*a*c))/(2*a))


# import math
# a=-1
# b=1
# c=2
# delta=b**2-4*a*c
# print((-b+math.sqrt(delta))/(2*a))
# print((-b-math.sqrt(delta))/(2*a))

#control +/ 取注释
# """"东方人的人格"""  取注释




# 数据类型
# 字符串 str 双引号或单引号包裹
# eg:len('Hello') 5  len('呦！') 2    len('hi!!') 4    len('6') 3  len('\n') 1  len('hi!!\n') 5
# "Hello"[4]  01234 4为o
# 布尔类型(bool) 真True  假False
# 空值类型(None)  表示完全没有值或不知道的值 my_wife=None
# 不确定某个对象类型时  用  type 函数 会返回你该对象的类型


# 对字符串求长度
s="Hello world!"
print(len(s))

# 通过索引获取单个字符
print(s[0])
print(s[11])

print(s[len(s)-1])

# 布尔类型
b1=True
b2=False

# 空值类型
n=None

# type函数
print(type(s))

print(type(b1))

print(type(n))
print(type(1.5))


# 测试代码
print("✨ 恭喜！你的 Python 环境配置成功啦！")
print("这是一条测试消息，说明解释器已经可以正常工作了 🎉")