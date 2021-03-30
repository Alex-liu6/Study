###     容器类型数据   set 和 dict


### set  集合    用来做交叉互补 集合操作的
'''
自动去重、无序
'''

# 定义一个空集合
set_var = set()      #{ } 不是集合    而是一个字典
print(set_var,type(set_var))
'''
运行结果是：
set() <class 'set'>
'''

# 自动去重、无序
str_var = {"a","b","c","d"}
print(str_var)
'''
运行结果是：
{'a', 'b', 'c', 'd'}
再次运行结果是：
{'c','b', 'a', 'd'}
再次运行结果是：
{'d', 'c', 'b', 'a'}
'''

str_var = {"a","a","b","b","c","d","d"}
print(str_var)
'''
运行结果是：
{'c', 'a', 'd', 'b'}
'''


# 既不可获取 也不可修改
str_var = {"a","b","c","d"}
alex = str_var[0]
print(alex)
'''
运行结果是：
error
'''

