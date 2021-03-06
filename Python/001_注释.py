###注释就是对代码的解释，为了方便阅读代码使用
###注释的分类 ：
#（1）单行注释：就是在代码行前加#号
#（2）多行注释：''' 文本'''  或者    """文本""" 
#方式一
'''
print("船员们经常往返于这条布遍灯塔的水路")
print("其中很多船员是坐着穿越吉利海峡的船而来的")
print("大海")
'''
#方式二
"""
print("船员们经常往返于这条布遍灯塔的水路")
print("其中很多船员是坐着穿越吉利海峡的船而来的")
print("大海")
"""

###注释的注意点
'''
注释嵌套的时候，需要注意
如果外边是三个单引号，则里边用三个双引号
如果外边是三个双引号，则里边用三个单引号
'''
#方式一
'''
print("船员们经常往返于这条布遍灯塔的水路")
"""
print("其中很多船员是坐着穿越吉利海峡的船而来的")
"""
print("大海")
'''
#方式二
"""
print("船员们经常往返于这条布遍灯塔的水路")
'''
print("其中很多船员是坐着穿越吉利海峡的船而来的")
'''
print("大海")
"""


#执行时可以将注释符取消，并观察注释前后的变化
