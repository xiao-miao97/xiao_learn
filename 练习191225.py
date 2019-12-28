'''
华氏温度转换为摄氏温度

'''

f = float(input('请输入华氏温度：'))
c = (f - 32) /1.8

print('%.1f华氏温度 = %.1f摄氏温度' % (f, c))


'''
输入圆的半径计算周长和面积

'''
import math # math是常用数学函数库，math.pi是圆周率

r = float(input('请输入圆的半径: '))
z = r ** 2 * math.pi
y = 2 * math.pi * r

print('圆的周长为%.2f,面积为%.2f' % (y, z))

'''
math中常用数学函数
    ceil(x) 取顶
    floor(x) 取底
    fabs(x) 取绝对值
    factorial(x) 阶乘
    hypot(x,y) sqrt(x*x+y*y)
    pow(x,y) x的y次方
    sqrt(x) 开平方
    log(x)
    log10(x)
    trunc(x) 截断取整数部分
    isnan (x) 判断是否NaN(not a number)
    degree (x) 弧度转角度
    radians(x) 角度转弧度
    e = 2.718281828459045
    pi 圆周率
'''
########################################################

'''
输入年份，闰年输出True，否则输出False

'''

year = int(input('请输入年份：'))
f = (year % 4 == 0 and year % 100 != 0) or \
    year % 400 == 0
'''
"\"的作用：
    1.后跟字符表示转义字符，如\n表示换行
    2.续行，如果一行太长了想分行，在第一行后加空格\，就可以把剩下的写到第二行。 
'''

print(f)