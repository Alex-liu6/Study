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













