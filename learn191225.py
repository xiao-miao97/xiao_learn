################################################################
a = 300
b = 23

print(a + b)
print(a / b)
print(a * b)
print(a - b)
print(a // b)
# 整除 - 返回商的整数部分（向下取整）9//2 得到4 ；-9//2 得到-5
print(a % b)
print(a ** b)



a = 100
b = 12.325
c = 1 + 5j
d = 'Hello World'
e = True
'''布尔值首字母大写，例如“True”'''

print(type(a))
print(type(b))
print(type(c))
'''
complex 复数类型
结构：a+-bj
     其中a是实部，b是虚部，j为b的标志符号
'''
print(type(d))
print(type(e))

########################################################################

a = int(input('a= '))
b = int(input('b= '))

print('%d + %d = %d' % (a, b, a+b))
'''
占位符语法：
    %d: 既可以表示字符串str，还可以表示整数int，浮点float
    %f: 既可以表示浮点float，还可以表示整数int（默认保留6位小数
    %%：百分号
    %s: 既可以表示字符串，还可以表示整数int，浮点float
    若想自主保留n位小数，%.nf

格式：
    print('含有占位符的格式' % （变量）)
    例如：   userName = '张三'
            print('姓名：%s' % (userName))
'''

#########################################################
'''
赋值运算符和复合赋值运算符
'''

a = 10
b = 3

a += b #相当于a = a + b
a *= a + 2 #相当于b = b * (b + 2)
print(a)

############################################################

'''
比较、逻辑和身份运算的使用

    逻辑运算符：not, or, and
    身份运算符：in，not in
'''

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not(1 != 2)

print('flag0 =', flag0)
print('flag1 =', flag1)
print('flag2 =', flag2)
print('flag3 =', flag3)
print('flag4 =', flag4)
print('flag5 =', flag5)
print(flag1 is True)
print(flag2 is not False)
#返回True or False