### 容器类型 （str   list   tuple   set   dict）

# 定义一些变量
var1 = "good good study"
var2 = [1,2,3]
var3 = (4,5,6)
var4 = {"a","b"}
var5 = {"c" : 66, "d" : 77}
var6 = 888



# str （容器类型数据或Number类型数据都可以）
alex = str(var2)
print(alex)
'''
运行结果是：
[1, 2, 3]
'''
alex = str(var3)
print(alex)
'''
运行结果是：
(4, 5, 6)
'''
alex = str(var4)
print(alex)
'''
运行结果是：
{'b', 'a'}
'''
alex = str(var5)
print(alex,type(alex))
'''
运行结果是：
{'c' : 66, 'd' : 77} <class 'str'>
'''
alex = str(var6)
print(alex)
'''
运行结果是：
888
'''


# 可以从var5的type看出已经强制转换成了 str ，但是并不是字符串的格式
# repr 以字符串形式原型化输出数据（产生引号）
alex = str(var5)
print(repr(alex),type(alex))
'''
运行结果是：
"{'c' : 66, 'd' : 77}" <class 'str'>
'''




# list   
'''
如果是字符串，把字符串中的每一个字符当成新的元素放到列表中
如果是其他数据，就是单纯的把原标识换成 [ ]
'''
alex = list(var1)
print(alex)
'''
运行结果是：
['g', 'o', 'o', 'd', ' ', 'g' , 'o', 'o', 'd', ' ', 's', 't', 'u', 'd', 'y']
'''
alex = list(var3)
print(alex)
'''
运行结果是：
[4, 5, 6]
'''
alex = list(var4)
print(alex)
'''
运行结果是：
['a', 'b']
'''
alex = list(var5)
print(alex)
'''
运行结果是：
['c', 'd']                 #强转字典时，保留键，舍去值
'''
alex = list(var6)
print(alex)
'''
运行结果是：
error
'''



# tuple
'''
如果是字符串，把字符串中的每一个字符当成新的袁旭放到元组中
如果是其他数据，就是单纯的把原标识符换成 ( )    变成元组即可
'''
alex = tuple(var1)
print(alex)
'''
运行结果是：
('g', 'o', 'o', 'd', ' ', 'g' , 'o', 'o', 'd', ' ', 's', 't', 'u', 'd', 'y')
'''
alex = list(var2)
print(alex)
'''
运行结果是：
(1, 2, 3)
'''
alex = list(var4)
print(alex)
'''
运行结果是：
('a', 'b')
'''
alex = list(var5)
print(alex)
'''
运行结果是：
('c', 'd')                 #强转字典时，保留键，舍去值
'''
alex = list(var6)
print(alex)
'''
运行结果是：
error
'''





# set
'''
如果是字符串，把字符串中的每一个字符当成新的元素放到集合中
如果是其他数据，就是单纯的把原标识换成 { } 变成集合
'''

alex = set(var1)
print(alex)
'''
运行结果是：
{'t', ' ', 'd', 'g', 'u', 'y', 's', 'o'}       #因为无序，字符串被打算，且去重会将重复的字符舍去
'''
alex = set(var2)
print(alex)
'''
运行结果是：
{1, 2, 3}
'''
alex = set(var3）
print(alex)
'''
运行结果是：
{4, 5, 6}
'''
alex = set(var4)
print(alex)
'''
运行结果是：
{'a', 'b'}
'''
alex = set(var5)
print(alex)
'''
运行结果是：
{'c', 'd'}                 #强转字典时，保留键，舍去值
'''
alex = set(var6)
print(alex)
'''
运行结果是：
error
'''

           
# 过滤列表重复数据
list_var = [1,2,3,4,5,5,6,7,6]
container = set(list_var)
print(container)
'''
运行结果是：
{1， 2， 3， 4， 5， 6， 7}
'''
container = list(container)
print(container,type(container))
'''
运行结果是：
[1, 2, 3, 4, 5, 6, 7] <class 'list'>
'''
           
