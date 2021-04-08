### 容器类型数据 （Str   List   Tuble   Set   Dict）

'''
转义字符： \
（1）将有意义的字符变得无意义
（2）将无意义的字符变得有意义

\r\n   \n 两个都代表换行
\t   代表缩进（水平制表符）
\r   代表将后面的字符拉到当前行 行首

可以用 \ 把有意义的引号变的无意义
'''


### str 字符串类型
'''
用引号引起来的数据就是字符串
'''

## 单引号
str_var = 'hello world !'
print(str_var,type(str_var))
'''
运行结果是：
hello world ！ <class 'str'>
'''

## 双引号
str_var = "good good study, day day up"
print(str_var,type(str_var))
'''
运行结果是：
good good study, day day up <class 'str'>
'''

str_var = "good good study, \nday day up"
print(str_var,type(str_var))
'''
运行结果是：
good good study,
day day up <class 'str'>
'''

str_var = "good good study, \tday day \r\nup"
print(str_var,type(str_var))
'''
运行结果是：
good good study,  day day          day字符前会有一个明显的缩进字符
up <class 'str'>
'''

str_var = "good good study, \rday day up"
print(str_var,type(str_var))
'''
运行结果是：
day day up <class 'str'>
'''

str_var = "good good "study", day day up"
print(str_var,type(str_var))
'''
运行结果是：
error
'''
#需要做如下修改
str_var = "good good \"study\", day day up"
print(str_var,type(str_var))
'''
运行结果是：
good good "study", day day up <class 'str'>
'''


## 三引号      支持跨行，无需对单双引号重新转义
str_var = """good good study,
day day up """
print(str_var,type(str_var))
'''
运行结果是：
good good study,
day day up <class 'str'>
'''

str_var = '''good good "study",
day 'day' up '''
print(str_var,type(str_var))
'''
运行结果是：
good good "study",
day 'day' up <class 'str'>
'''



### 元字符串      原型化输出字符串，让转义字符失效
str_var = r"good good study, \rday day up"
print(str_var)
'''
运行结果是：
"good good study, /rday day up"
'''





### 字符串的格式化
# %d   %f   %s    
#语法：  "字符串%d"   % (值)

## %d 整形占位符
str_var = "I have %d sports cars" % (10)
print(str_var)
'''
运行结果是：
I have 10 sports cars
'''
## %2d 默认数字居右

## %-2d 默认数字居左



## %f 浮点型占位符      默认小数点后面保留6位
str_var = "I spend %f dollars a day" % (9.99)
print(str_var)
'''
运行结果是：
I spend 9.990000 dollers a day
'''
# %.1f  存在四舍五入
str_var = "I spend %.1f dollars a day" % (9.99)
print(str_var)
'''
运行结果是：
I spend 10.0 dollars a day
'''
# %.3f  保留小数点后3位
str_var = "I spend %.3f dollars a day" % (9.99)
print(str_var)
'''
运行结果是：
I spend 9.990 dollars a day
'''



## %s 字符串占位符
str_var = "%s" % ("good good study day day up")
print(str_var)
'''
输出结果是：
good good study day day up
'''



#综合案例
str_var = "I am a network engineer, %d yuan a month, spend %.1f yuan a day, life is %s" % (100000,9.99,"very comfortable")
print(str_var)
'''
输出结果是：
I am a network engineer, 100000 yuan a month, spend 10.0 yuan a day, life is very comfortable
'''

