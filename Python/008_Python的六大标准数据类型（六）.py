### 容器类型数据 set和 dict

### dict 字典       由键值对数据组成   无序
'''
语法：
dict_var = {'a' : 1}
"键" ： "值"  键和值之间用冒号隔开，键值对之间用逗号隔开
'''
'''
在3.6版本之前，字典无序
在3.6版本之后，字典有序（看起来有序，实则无序）

这里看起来有序使用的就是哈希算法，
哈希算法：
    将不可变的任意长度值计算成具有固定长度的唯一值，这个值可正可负，可大可小，通过计算键，来获取值，形成一一映射的效果
    管这个算法叫哈希算法，管这个值叫哈希值
    
    字典进行存储时，并不一定按照字面顺序依次存在内存中，而是通过哈希算法，随机散列的把键所对应的值存储在内存中，所以字典无序（这样做的目的则是为了图快）
    可以通过哈希算出的键获取散列的值
    
    3.6之后，记录了字典的字面顺序，再取出数据时，进行重新排序，所以看起来有序（但本质上无序）
'''

'''
可哈希数据（不可变的数据）：Number(int,float,complex,bool)  str  tuple
不可哈希数据（可变的数据）：list  set  dict  （list  dict 值可变；set 顺序可变）

字典的键    集合的值   都需要可哈希数据，剩下的数据无所谓
'''


# 定义一个空字典
dict_var = {}
print(dict_var,type(dict_var))
'''
运行结果是：
{} <class 'dict'>
'''


# 
dict_var = {"xiaoming" : 66, "xiaogang" : 75, "xiaolv" : 88, "xiaoxiao" : 100}
print(dict_var,type(dict_var)
'''
运行结果是：
{'xiaoming': 66, 'xiaogang' : 75, 'xiaolv' : 88, 'xiaoxiao' : 100} <class 'dict'>
'''

# 获取字典当中的值（通过键来获取值）
alex = dict_var['xiaolv']
print(alex)
'''
运行结果是：
88
'''

# 通过字典的键来修改值
dict_var['xiaolv'] = 100
print(dict_var)
'''
运行结果是：
{'xiaoming': 66, 'xiaogang' : 75, 'xiaolv' : 100, 'xiaoxiao' : 100}
'''

'''
字典的键唯一，如果两个键相同，后面的覆盖前面的

字典的键是唯一不可修改的，字典的值随意
'''

dict_var = {"a" : 1, "a" : 2}
print(dict_var)
'''
运行结果是：
{'a' : 2}
'''

