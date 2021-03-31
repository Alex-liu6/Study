### 二级容器，外面是一个容器类型数据，里面的元素还是一个容器类型数据
# 二级容器
list_var = [1,2,3,(4,5,6)]
print(list_var,type(list_var))
'''
运行结果是：
[1, 2, 3, (4, 5, 6)] <class 'list'>
'''


# 二级列表
list_var = [1,2,3,[4,5,6]]
print(list_var,type(list_var))
'''
运行结果是：
[1, 2, 3, [4, 5, 6]] <class 'list'>
'''


# 二级元组
tuple_var = (2,4,(6,8,10))
print(tuple_var,type(tuple_var))
'''
运行结果是：
(2, 4, (6, 8, 10)) <class 'tuple'>
'''


# 二级集合             只能存放元组
set_var = {1,2,3,(4,5,6)}
print(set_var,type(set_var))
'''
运行结果是：
{1, 2, 3, (4, 5, 6)} <class 'set'>
'''

# 二级字典
dict_var = {'a' : {'c' : 66},'b' : 88}
print(dict_var,type(dict_var))
'''
运行结果是：
{'a' : {'c' : 66}, 'b' : 88} <class 'dict'>
'''
# 如何在二级字典中取值呢？取出66
alex = dict_var['a']['c']
print(alex)
'''
运行结果是：
66
'''

# 那如果是多级容器怎么取值呢？
alex666 = [1,2,3,(4,5,6,{"a" : 1,"b" : [7,8,9]}),66]
# 取出8
alex = alex666[-2][-1]["b"][-2]    #使用逆向索引
print(alex)
'''
运行结果是：
8
'''


# 等长的二级容器
'''
1.里面每个元素都是容器类型数据
2.每个容器类型数据的元素个数都相同
example = [(1,2,3),[4,5,6]]
'''

### 字典的强制转换
'''
需要等长的二级容器，而且每个容器里面的元素只能是两个
'''

# （1）外面是列表，里边是列表或元组或字符串
var1 = [["a",1],("b",2),"good"]
alex = dict(var1)
print(alex)
'''
运行结果是：
error            #字符串慎用，如果值是多个，有局限性
'''
var2 = [["a",1],("b",2)]
alex = dict(var2)
print(alex,type(alex))
'''
运行结果是：
{'a' : 1, 'b' : 2} <class 'dict'>       #推荐此种方法
'''


# （2）外面是元组，里面是列表元组或字符串
var1 = (["c",11],("d",22))
alex = dict(var1)
print(alex,type(alex))
'''
运行结果是：
{'c' : 11, 'd' : 22} <class 'dict'>      #推荐此种方法
'''

# 注意，如果往列表或者元组容器放集合，语法上不报错，但情况出乎意料，达不到我们想要看到的字典的格式,因为集合无序
example = dict([{"a",1},{"b",2}])
print(example,type(example))
'''
运行结果是：
{'a' : 1, 2 : 'b'} <class 'dict'>
再运行一次：
{1 : 'a', 'b' : 2} <class 'dict'>
'''

# （3）外面是集合，里面是元组或字符串
var1 = {("a",1),("b",2),"c3"}          #必须放入不可变数据，即可哈希
alex = dict(var1)
print(alex)
'''
运行结果是：
{'a' : 1, 'c' : 3, 'b' : 2}
'''



'''
int()   float()   bool()   comp[lex()
str()   list()   tuple()   set()   dict()
这些函数在进行强转时，都默认转化成当前的数据类型
用这样的方式也可以初始化一个值
'''
alex = int()
alex = list()
print(alex)
