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

#水仙花数
Number = input('请输入一个数字:')
bai = int(Number[0])
shi = int(Number[1])
ge = int(Number[2])
if bai **3 + shi **3 + ge **3 == int(Number):
    print('是水仙花')
else:
    print('不是水仙花')
#输入一个年份，判断是否是闰年
year = int(input('请输入年份=>>'))
if (year % 4 == 0 and year % 100 != 0 or year% 400==0):
    print('%d 是闰年'%year)
else:
    print('%d 不是闰年'%year)
#  MD5加密    
import hashlib
str = '666@qq.com'
m = hashlib.md5()
b = str.encode(encoding='utf-8')
m.update(b)
str_md5 = m.hexdigest()
print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + str_md5)
#输入一个年份，判断是否是闰年
year = int(input('请输入年份=>>'))
if (year % 4 == 0 and year % 100 != 0 or year% 400==0):
    print('%d 是闰年'%year)
else:
    print('%d 不是闰年'%year)

#输入一个月份判断有多少天
a = eval(input('请输入月份：'))
 
while not(isinstance(a, int) and 0<a<13):
    a = eval(input('请输入正确的月份：'))
 
da = [1,3,5,7,10,12]
xiao = [4,6,8,9,11]
 
if (a in da):
    print(a,'月有31天')
elif (a in xiao):
    print(a,'月有30天')
else:
    n=eval(input('请输入月所在年：'))
    if  n%400==0 or (n%4==0 and n%100!=0):
        print(n,'年为闰年',a,'月有29天')
    else:
        print(n,'年为平年',a,'月有28天')

