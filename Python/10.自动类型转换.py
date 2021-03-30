### 自动类型转换 针对于Number类型 bool float int complex

'''
当Number类型中不同的数据类型进行运算的时候，默认向更高精度转化
精度从低到高依次顺序是：
bool -> int -> float -> complex
True 默认转化是1
False 默认转化是0
'''

# （1）bool + int
alex = True + 99 
print(alex)
'''
运行结果是：
100
'''

#（2）bool + float
alex = True + 3.3
print(alex)
'''
运行结果是：
4.3
'''

#（3）bool + complex
alex = False + 3+4j
print(alex)
'''
运行结果是：
(3+4j)
'''

# （4）int + float
alex = 66 + 3.3
print(alex)
'''
运行结果是：
69.3
'''

# （5）int + complex
alex = 66 + 3+4j
print(alex)
'''
运行结果是：
(69+4j)
'''

# （6）float + complex
alex = 3.3 + 3+4j
print(alex)
'''
(6.3+4j)
'''
