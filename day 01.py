#01 温度转换 
c = float(input('请输入摄氏温度: '))
f =  (c*1.8)+32
print('%.1f摄氏度 = %.1f华氏度' % (c, f))


#02 圆柱体的体积和表面积
import math
radius = float(input('请输入圆柱的半径: '))
length = float(input ('请输入圆柱的高: '))
area = radius * radius * math.pi
volume = area * length
print('表面积: %.2f' % area)
print('体积: %.2f' % volume)


#03 长度转换
feet=float(input('请输入英尺数： '))
meters=feet *0.305
print('%.1f英尺 = %.4f米' % (feet,meters))


#04 计算能量
M = float(input('请输入水量(以千克为单位)：'))
initialTemperature = float(input('请输入初始温度(摄氏度): '))
finalTemperature = float(input('请输入最终温度(摄氏度): '))
Q = M * (finalTemperature - initialTemperature) * 4184
print('所需能量为: %.1f' %Q )


#05 计算利息
balance =float(input('请输入差额：'))
interestRate =float(input('请输入年利率：')) 
interest = balance *(interestRate/1200)
print('下个月月供利息为: %.5f' %interest)


#06 加速度
V0 = float(input('请输入初速度(以米为秒为单位)：'))
V1 = float(input('请输入末速度(以米为秒为单位): '))
t = float(input('请输入单位速度变化所用时间(以秒为单位): '))
a = (V1-V0)/t
print('平均加速度为: %.4f' %a )


#07 复利值
cks = float(input('请输入每月存款数：'))
interestRate = 0.05 / 12
interest = 1 + interestRate
count =[0]
for i in range(6):
 month = (100 + count[i]) * interest
 count.append(month)
print('六个月后的账户总额为：%.2f' % count[6])


#08 求和
num = int(input('请输入1-1000的一个整数：'))
ge = int(num % 10)
shi = int(num //10 % 10)
bai = int(num //100)
sum = ge + shi + bai
print('各位数字之和：',sum)

# #001 五边形面积
import math
r = float(input('请输入五边形顶点到中心的距离：'))
side = 2 * r * math.sin(math.pi/5)
Area = 5 * side ** 2 / (4 * math.tan(math.pi/5))
print('这个五边形的面积为：%.2f'%Area)


#002 大圆距离
import math
x1,y1 = eval(input('Please input point1(latitude and longitude) in degrees:'))
x2,y2 = eval(input('Please input point2(latitude and longitude) in degrees:'))
radius = 6371.01
x11 = math.radians(x1) #math.radians()函数将度数转换成弧度数
y11 = math.radians(y1)
x22 = math.radians(x2)
y22 = math.radians(y2)
d = radius * math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11-y22))
print('The distance between the two points is %5.2f km'%d)


#003 五角形的面积
 import math
 s = float(input('请输入五角形的边长：'))
 Area = (5*s*s)/(4*math.tan(math.pi/5))
 print('五角形的面积为：%f'%Area)

 
#004 一个正多边形的面积
 import math
 s = float(input('请输入正多边形的边长：'))
 n = float(input('请输入多边形有几条边：'))
 Area = (n*s*s)/(4*math.tan(math.pi/n))
 print('正多边形的面积为：%f'%Area)


#005 找出ASCII码的字符
 a = int(input('请输入一个ASSCII码(0-127):'))
 print(chr(a))


#006 工资表
 name = input('Enter employee\'s name:\000\000') 
 number = int(input('Enter number of hours worked in a week:\000\000')) 
 pay = float(input('Enter hourly pay rate:\000\000')) 
 federal = float(input('Enter federal tax withholding rate:\000\000')) 
 state = float(input('Enter state tax withholding rate:\000\000')) 
 print('Employee Name:\000'+name) 
 print('Hours worked:\000%.1f'%(float(number))) 
 print('Pay Rate:\000$'+str(pay)) 
 print('Gross Pay:\000$'+str(number*pay)) 
 print('Deductions:\n\000Federal Withholding(20.0%):\000$'+str(number*pay*0.2)+'\n\000State Withholding(9.0%):\000$'+ 
 str(number*pay*0.09)+'\n\000Total Deduction:\000$%.2f'%((number*pay*0.2)+(number*pay*0.09))) 
 print('Net Pay:\000$%.2f'%(((number*pay)-((number*pay*0.2)+(number*pay*0.09))))) 


#007 反向数字
 a = input('请输入一个四位数整数：')
 print(a[::-1])

 
#008 加密
 import hashlib
 m = hashlib.md5()
 a = input('请输入字符串：')
 m.update(bytes(a,encoding='utf8'))
 with open('password.txt','w')as file:
     file.write(m.hexdigest())
 print(m.hexdigest())
