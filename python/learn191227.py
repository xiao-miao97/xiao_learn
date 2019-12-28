"""
for循环实现1~100求和
"""

x = 0
for y in range(100):
    x += y
print(x)

# range(101) 可以产生一个0到100的整数序列
# range(1,100) 可以产生一个1到99的整数序列
# range(1,100,2) 可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量

'''
1~100之间的偶数求和
'''
# 循环
x = 0
for y in range(2, 101, 1):
    x += y
print(x)

# 分支结构
x = 0
for y in range(1, 101):
    if x % 2 == 0:
        x += y
print(x)

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

"""

# 如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环

import random
# random() 方法返回随机生成的一个实数，它在[0,1)范围内。

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了！')
        break   # break只能终止它所在的那个循环
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')

'''
九九乘法表

'''

for x in range(1, 10):
    for y in range(1, x+1):
        print('%d * %d = %d' % (x, y, (x * y)), end='\t')
        # end="" 可使输出不换行
        # \t代表制表符，end=说明打印后跟空格，即下一个打印接着后面输出。默认是换行，会在下一行输出下一个内容
    print(end='\n')