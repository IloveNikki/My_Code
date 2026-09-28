# 购物清单
shopping_list=[]
shopping_list.append("键盘")
shopping_list.append("键帽")
# 此时打出来的为上面两个，若想去除一个，即敲出下一行代码
shopping_list.remove("键帽")
shopping_list.append("音响")
shopping_list.append("电竞椅")
# 更改元素
shopping_list[1]="硬盘"

# print(shopping_list)
# # 用len函数输出有多少函数
# print(len(shopping_list))
# # 获得某个位置的元素
# print(shopping_list[0])
price=[799,1024,200,800]
# 最大最小
max_price=max(price)
min_price=min(price)
# 排序
sorted_price=sorted(price)
print(max_price)
print(min_price)
print(sorted_price)