###变量：可以改变的量就是变量；具体指的是内存的一块空间
beizi = "水"
print（beizi）
beizi = "茶"
print（baizi）


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




