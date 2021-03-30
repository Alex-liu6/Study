### 强制类型转换 Number ---> int  float  bool  complex

# 定义一些变量
var1 = 66
var2 = 9.9
var3 = True
var4 = False
var5 = 5+8j
var6 = "good"
var7 = "123456"



# 把数据强制转换成整型 int  （只支持强制转换为：整型、浮点型、布尔类型、纯数字字符串）
alex = int(var2)
print(alex)
'''
运行结果是：
9
'''
alex = int(var3)
print(alex)
'''
运行结果是：
1
'''
alex = int(var4)
print(alex)
'''
运行结果是：
0
'''
alex = int(var5)
print(alex)
'''
运行结果是：
error          # 不能强制转换哦
'''
alex = int(var6)
print(alex)
'''
运行结果是：
error
'''
alex = int(var7)
print(alex)
'''
运行结果是：
123456
'''



# float   (只支持强制转换为：整型、浮点型、布尔型、纯数字字符串)
alex = float（var1）
print(alex)
'''
运行结果是：
66.0
'''
alex = float（var3）
print(alex)
'''
运行结果是：
1.0
'''
alex = float（var4）
print(alex)
'''
运行结果是：
0.0
'''
alex = float（var5）
print(alex)
'''
运行结果是：
error
'''
alex = float（var6）
print(alex)
'''
运行结果是：
error
'''
alex = float（var7）
print(alex)
'''
运行结果是：
123456.0
'''




# complex    （只支持强制转换为：整型、浮点型、布尔型、纯数字字符串、复数）
alex = complex(var1)
print(alex)
'''
运行结果是：
(66+0j)
'''
alex = complex(var2)
print(alex)
'''
运行结果是：
(9.9+0j)
'''
alex = complex(var3)
print(alex)
'''
运行结果是：
(1+0j)
'''
alex = complex(var4)
print(alex)
'''
运行结果是：
0j
'''
alex = complex(var6)
print(alex)
'''
运行结果是：
error
'''
alex = complex(var7)
print(alex)
'''
运行结果是：
(123456+0j)
'''




# bool (可以将容器类型数据或Number类型数据进行强制转换，要么True，要么False)
alex = bool(var1)
alex = bool(var2)
alex = bool(var3)
alex = bool(var5)
alex = bool(var6)
alex = bool(var7)
print(alex)
'''
运行结果皆为：
True
'''
alex = bool([1,2,3])
print(alex)
'''
运行结果是：
True
'''

# bool为假的十种情况
'''
0   0.0   False   0j   ""   []   ()   set()   {}   None
None 是系统的一个关键字，表示空的，什么也没有，一般做初始值
'''

