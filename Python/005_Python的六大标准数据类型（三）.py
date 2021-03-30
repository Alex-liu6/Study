### 容器类型数据 list tuple

### list      可获取，可修改，有序
# （1）定义一个空列表
list_var = []
print(list_var,type(list_var))
'''
输出结果是：
[] <class 'list'>
'''
list_var = [11,3.1415,True,4-3j,"i have a apple"]
print(list_var,type(list_var))
'''
输出结果是：
[11, 3.1415, True, (4-3j), 'i have a apple'] <class 'list'>
'''

## 索引
# 正向索引   0    1     2    3        4
list_var = [11,3.1415,True,4-3j,"i have a apple"]
# 反向索引   -5   -4   -3    -2       -1

# （2）获取当前列表的值
alex = list_var[3]      #正向索引
print(alex)
'''
输出结果是：
(4-3j)
'''
alex = list_var[-3]      #反向索引
print(alex)
'''
输出结果是：
True
'''

"""
通用的想要获取列表最后一个元素值，需要通过 len 函数
len 用来获取容器类型数据的元素个数（长度）
"""
list_var = [11,3.1415,True,4-3j,"i have a apple"]
alex = len(list_var)
print(alex)
'''
输出结果是：
5
'''
#如果想要获取最后一个值，需要-1，因为正向索引是从0开始的
list_var = [11,3.1415,True,4-3j,"i have a apple"]
print(list_var[len(list_var)-1])      #等同于 print(list_var[4])
'''
输出结果是：
i have a apple
'''

# （3）修改列表中的值
list_var = [11,3.1415,True,4-3j,"i have a apple"]
list_var[1] = "3.1415926"
print(list_var[1])
'''
运行结果是：
3.1415926
'''

list_var[-2] = "666"
print(list_var[-2])
'''
运行结果是：
666
'''
