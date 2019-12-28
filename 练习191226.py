
# 英制单位英寸与公制单位厘米互换


value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%f英寸等于%f厘米' % (value, 2.54 * value))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米等于%.2f英寸' % (value, value / 2.54))
else:
    print('请输入有效单位！')

######################################################################

'''
百分制成绩转换为等级制成绩

'''

score = int(input('请输入您的成绩：'))
if score >= 90:
    grade = 'A'
elif score > 80:
    grade = 'B'
elif score > 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

print('对应的等级是：', grade)

###############################################################

# 输入三条边长，如果能构成三角形就计算周长和面积

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长等于', (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积：%f' % area)
else:
    print('不能构成三角形！')