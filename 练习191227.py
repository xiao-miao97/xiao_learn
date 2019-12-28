"""
输入一个正整数判断是不是素数
"""
import math

num = int(input('请输入一个正整数：'))
end = int(math.sqrt(num))
# sqrt()方法返回数字x的平方根, sqrt()是不能直接访问的，需要导入 math 模块
is_prime = True

for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 0:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

'''
输入两个正整数，计算他们的最大公约数和最小公倍数

'''

x = int(input('x = '))
y = int(input('y = '))

if x > y:
    x, y = y, x
    # 如果x大于y，交换x和y的值
for factor in range(x, 0, -1): # 从较小的数开始做递减循环
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break

'''
打印三角形图案
'''

row = int(input('请输入行数：'))
for i in range(row):
    for j in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()