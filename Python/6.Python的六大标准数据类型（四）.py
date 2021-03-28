### tuple      元组
'''
可获取、不可修改、有序

证明一个元组的根本特征是逗号，声明一个空元组，可以直接使用 () , (1)表明一个整形
'''

# 声明一个空元组
tuple_var = ()
print(tuple_var,type(tuple_var))
'''
运行结果是：
((), <class 'tuple'>)
'''

# 
tuple_var = (1,2,3,4)
print(tuple_var,type(tuple_var))
'''
运行结果是：
((1,2,3,4), <class 'tuple'>)
'''

tuple_var = (1,)
print(tuple_var,type(tuple_var))
'''
运行结果是：
((1,), <class 'tuple'>)
'''

tuple_var = 1,2,3
print(tuple_var,type(tuple_var))
'''
运行结果是“
((1,2,3), <class 'tuple'>)
'''

## 获取最后一个值
# 正向索引     0   1   2   3
tuple_var = ("a","b",True,666)
# 反向索引    -4  -3  -2  -1
alex = tuple_var[-1]
print(alex)
'''
运行结果是：
666
'''
alex = tuple_var[len(tuple_var)-1]
print(alex)
'''
运行结果是：
666
'''



## 修改一个值
tuple_var = ("a","b",True,666)
tuple_var[-2] = False
print(tuple_var)
'''
运行结果是：
error            #元组不可修改
'''










