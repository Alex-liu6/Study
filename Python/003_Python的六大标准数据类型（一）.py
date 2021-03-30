### Number 数值类型
#包含四种类型：int   float   bool   complex


### int 整型  （包含三种：正整型   0   负整型）
int_var = 666
print(int_var)
'''
运行结果是：
666
'''

## type 获取一个变量的类型   type（值）
alex = type(int_var)
print(alex)
'''
运行结果是：
<class 'int'>
'''

## id 获取该变量所指向值的地址 id（值）
alex = id(int_var)
print(alex)
'''
运行结果是：
2452706912080    该参数主要是表明变量存在内存中的ID
'''





### float 浮点型  也就是小数
#表达一
float_var = 3.15
print(float_var,type(float_var))
'''
运行结果是：
3.15 <class 'float'>
'''

#表达二
float_var = 5.35e-3
print(float_var,type(float_var))
'''
运行结果是：
0.00535 <class 'float'>            从返回值中可以看出小数点在原有数值的基础上往左移了三位
'''
float_var = 7.34e5
print(float_var,type(float_var))
'''
运行结果是：
734000.0 <class 'float'>            从返回值中可以看出小数点在原有数值的基础上往右移了五位
'''



### bool 布尔型  也就是True（真的）、False（假的）两种类型
bool_var = True
print(bool_var,type(bool_var))
'''
运行结果是：
True <class 'bool'>
'''
bool_var = False
print(bool_var,type(bool_var))
'''
运行的结果是：
False <class 'bool'>
'''



### complex 复数类型
"""
复数存放的是一对浮点数，一个表示实数部分，另一个表示虚数部分（跟随一个字母j）
j：如果一个数的平方等于-1，那么这个数就是j
（科学家认为有，表达一个高精度的类型）
"""
#方式一：
complex_var = 3+4j
print(complex_var,type(complex_var))
'''
运行结果是：
(3+4j) <class 'complex'>
'''

#方式二：  complex(实数,虚数)
complex_var = complex(-5,-2)
print(complex_var,type(complex_var))
'''
运行结果是：
(-5-2j) <class 'complex'>
'''

