#01 解一元二次方程
import math
d = 0
def gen(a,b,c):
    d = b*b - 4 * a * c
    if d > 0 :
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        print("该方程实根为 %f and %f"%(r1,r2))
    elif d == 0:
        r = -b / 2*a
        print("该方程实根为 %f"%r)
    else:
        print('该方程无实根')
def start():
    a,b,c = map(float,input('请输入a,b,c(用逗号分隔):').split(','))
    gen(a,b,c)
start()


#02 学习加法
import random
def Add(x):
    a = random.randint(0,100)
    b = random.randint(0,100)
    if x == a + b:
        print('True')
    else:
        print('False')
def Start():
    x = int(input('请输入两个随机数的和：'))
    Add(x)
Start()



#03 未来数据
def week(day):    
	    if day == 0:
	        print('星期日')
	    elif day == 1:
	        print('星期一')
	    elif day == 2:
	        print('星期二')
	    elif day == 3:
	        print('星期三')
	    elif day == 4:
	        print('星期四')
	    elif day == 5:
	        print('星期五')
	    elif day == 6:
	        print('星期六')
	        
	def today(day,day_1):
	    day_2 = day+day_1
	    if day_2>=7:
	        day_3 = (day_2)%7
	        week(day_3)
	    else:
	        week(day_2)
	    
	def sart():
	    day = eval(input('请输入今天是哪一天：'))
	    day_1 = eval(input('输入到哪天的天数'))
	    week(day)
	    today(day,day_1)
	sart()


#04 排序
def count(a,b,c):
	    num = [a,b,c]
	    num.sort()
	    print(num)
def start():
	    a = int(input('输入第一个整数：'))
	    b = int(input('输入第二个整数：'))
	    c = int(input('输入第三个整数：'))
	    count(a,b,c)
start()



#05 比较价钱

def shop(weight1,weight2,price1,price2):
	package1 = weight1 / price1
	package2 = weight2 / price2
	if package1 > package2:
	    print('亲，我建议您买第一种哦')
	else:
	    print('亲，我建议您买第二种哦')	
def start():
	weight1 = float(input('第一种重量是:')) 
	price1 = float(input('第一种价格是:'))
	weight2 = float(input('第二种重量是:'))
	price2 = float(input('第二种价格是:'))
	shop(weight1,weight2,price1,price2) 
start()  


#06 找天数
def start():
	year,month = map(int,input('输入年和月(逗号分隔)：').split(','))
	math(year,month)
	
def math(year,month):
    list1 = [1,3,5,7,8,10,12]
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month == 2:
            print('这个月有29天')
        elif month in list1:
            print('这个月有31天')
        else:
            print('这个月有30天')
    else:
        if month == 2:
            print('这个月有28天')
        elif month in list1:
            print('这个月有31天')
        else:
            print('这个月有30天')
        
start()



#07 头或尾
def start():
    x = int(input('请输入你的猜测（1为正，2为反）：'))
    math(x)

def math(x):
    a = random.randint(1,2)
    if x == a:
        print('你猜对了')
    else:
        print('你猜错了')

start()



#08 石头，剪刀，布
import random
def start():
    U_res = int(input('0:石头,1:剪刀,2:布>>>'))
    math(U_res)
def math(U_res):  
    C_res = random.randint(0,2)
    if C_res == U_res:
        print('平局')
    else:
        if C_res == 0 and U_res == 1:
            print('电脑赢了 ')
        elif C_res == 1 and U_res == 2:
            print('电脑赢了 ')
        elif C_res == 2 and U_res == 0:
            print('电脑赢了 ')
        else:
            print('你赢了 ')
start()


#09 一周的星期几
def main(year,m,d):
    a = ['周六','周日','周一','周二','周三','周四','周五']
    if m == 1:
        m = 13
        year = year - 1
    if m ==2:
        m = 14
        year = year - 1
    h = int(d+((26*(m+1))//10)+(year%100)+((year%100)/4)+((year//100)/4)+5*year//100)%7
    day = a[h]
    print('那一天是一周中的:%s' %day)
def Start():
    year = int(input('输入哪一年:'))
    m = int(input('输入月份1-12:'))
    d = int(input('输入月份第几天1-31:'))
    main(year,m,d)
Start()


#10 选牌
def chou():
    import numpy as np
    daxiao=np.random.choice(['A','2','3','4','5','6','7','8','9','10','J','Q','K'])
    huase=np.random.choice(['梅花','红桃','方块','黑桃'])
    print('你选择的牌是  %s , %s'%(huase,daxiao))
def Start():
    a = input("是否决定抽牌y/n:")
    if a == 'y':
        chou()
    else:
        pass
Start()


#11 回文数
def main(a):   
    b = a
    a2 = 0
    while b > 0:
        a2 *= 10
        a2 += b % 10
        b //= 10
    if a == a2:
        print('%d是回文数' % a)
    else:
        print('%d不是回文数' % a)
def start():
    a = int(input('请输入一个正整数: '))
    main(a)
start()


#12 三角形周长
def main(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        L = a+b+c
        print("其周长为",L)
    else:
        print("不是三角形三条边") 
def Start():
    a,b,c = map(float,input('请输入三条边长（逗号分隔）：').split(','))
    main(a,b,c)
Start()


#13 平均值
def main(x,zheng,fu,i,sum1):
    while x!=0:
        x = int(input('输入一个整数，以输入值0来结束：'))
        if(x>0):
            zheng += 1
        elif(x<0):
            fu += 1
        i += 1
        sum1 = sum1 + x
    if sum1 != 0:
        xxx = sum1/(i-1)
        print('输入的正数有%d个，输入的负数有%d个，这组数的和为%d，这组数的平均数为%.2f'%(zheng,fu,sum1,xxx))
    else:
        print('结束')
        return   
def start():
    x = 1
    zheng = 0
    fu = 0
    i = 0
    sum1 = 0
    main(x,zheng,fu,i,sum1)
        
start()


#14 未来学费
a = [1000]
for i in range(14):
    x = a[i] * 1.05
    a.append(x)
print('十年后的学费是：%.2f'%a[14])
print('现在及十年后的学费是：%.2f'%sum(a))


#15 整除
t = 0
for i in range(100,1000):
	if i % 5 == 0 and i % 6 == 0:
	    print(i,end = ' ')
	    t += 1
	if t % 10 == 0:
	    print()


#16 n
def main():
    n = 0
    m = 0
    math(n,m)
def math(n,m):
    while n**2 <= 12000:
        n += 1
    print('n的平方大于12000的最小整数n为：%d'%n)

    while m**3 < 12000:
        m += 1
    print('n的立方大于12000的最大整数n为：%d'%(m-1))
main()


#17 消除错误
def start():
    sum1 = 0
    sum2 = 0
    main(sum1,sum2)

def main(sum1,sum2):
    for i in range(1,50001):
        sum1 += 1/i
        i += 1
    print('从左向右计算为：',sum1)
    for i in range(50000,0,-1):
        sum2 += 1/i
        i -= 1
    print('从右向左计算为：',sum2)

start()


#18 数列求和
a = 1
b = 3
c = 0
while a >=1:
	c += a/b
	a += 2
	b += 2
	if a > 97:
	    print(c)
	    break


#19 π
i = 1
pi = 0
while i > 0:
	a = 4*((-1)**(i+1)/(2*i-1))
	i += 1
	pi += a
	if i % 10000 == 0:
	    print(pi)
	elif i > 10000:
	    break


#20 完全数
for i in range(1,10000):
    x = 0
    for j in range(1,i):
        if i % j == 0:
            x += j
    if x == i:
        print('10000以下的完全数有：%d'%x)


#21 组合
list1 = []
for i in range(1,8):
    for j in range(1,8):
            if i != j and sorted([i,j]) not in list1:
                list1.append([i,j])
print('所有可能的组合为：',list1)
print('组合总个数为：',len(list1))

