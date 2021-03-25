###变量：可以改变的量就是变量；具体指的是内存的一块空间
beizi = "水"
print（beizi）
beizi = "茶"
print（baizi）
#杯子加了水就是水杯；杯子加了茶就是茶杯；杯子就是变量！

###变量的声明
#方法一
a = 1
b = 2
print(a)
print(b)

#方法二
a,b = 3,4
print(a,b)

#方法三
a = b = 5
print(a,b)

###变量的命名
"""
打油诗：
         变量的命名
字母数字下划线，首字符不能为数字
严格区分大小写，且不能使用关键字
变量命名有意义，且不能使用中文字
"""

#如何查看有哪些关键字
#import 引入 keyword（模块名）
import keyword
test = keyword.kwlist   #定义变量test，赋予这个值，可以打印出所有的关键字，当然注意的是还不至这些关键字
print(test)
'''
返回如下值，皆为关键字
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

#命名要有意义
#用中文命名变量语法上允许，但严禁使用


###变量的交换
#通用的交换写法
a = 3
b = 4
var = a
a = b
b = var
print(a,b)

#python的写法
a = 3
b = 4
a,b = b,a
print(a,b)



