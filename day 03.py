# 01 五角数
# def getPentagonalNumber(n):
#     count = 0
#     for i in range(1,n+1):
#         num = i*(3*n-1)/2
#         print("%d"%num,end = ' ')
#         count += 1
#         if count % 10 ==0:
#             print('\n')
# getPentagonalNumber(100) 



# 02 求一个整数各个数字的和
# n = input('请输入整数：>>')
# w  =len(n)
# list_num =[]
# def sumDigits(n):
#     global w
#     global list_num
#     for i in range(len(n)):
#         f = int(n)%10
#         n = str(int(n)//10)
#         list_num.append(f)
#         w -=1
#         if w == 0:
#             sum_=sum(list_num)
#             print(sum_)
# sumDigits(n) 



# 03 对三个数排序
# def displaySortedNumbers(num1,num2,num3):
# 	    num = [num1,num2,num3]
# 	    num.sort()
# 	    print(num)
# def start():
# 	    num1 = int(input('输入第一个整数：'))
# 	    num2 = int(input('输入第二个整数：'))
# 	    num3 = int(input('输入第三个整数：'))
# 	    displaySortedNumbers(num1,num2,num3)
# start()


# 04 未来投资值

# 05 显示字符
# def printChars():
#     for i in range(73,91):
#         print(chr(i),end=" ")
#         if i% 10 == 0:
#             print("\n")
# printChars()



# 06 一年的天数
# def numberOfDaysInAYear(year):
#     for count in range(year,year+11):
#         if count % 4 == 0 and count % 100 != 0 or count % 400 == 0:
#             print("{}年有366天".format(count))
#         else:
#             print("{}年有365天".format(count))
# numberOfDaysInAYear(2010)


# 07 显示角
# import math
# def distance(x1,x2,y1,y2):
#     d =math.sqrt((x1-x2)**2+(y1-y2)**2)
#     print('两点间的距离为：%.2f' %d) 
# distance(2,3,4,5)

# 08 梅森素数


# 09 当前时间和日期
# import time
# def main():
#     localtime = time.asctime(time.localtime(time.time()))
#     print("本地时间为 :", localtime)
# main()


# 10 掷骰子
# import random
# def shaizi():
#     a=random.choice([1,2,3,4,5,6])
#     b=random.choice([1,2,3,4,5,6])
#     if a+b==2 or  a+b==3 or a+b==12:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('你输了')
#     elif a+b==7 or a+b==11:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('你赢了')
#     else:
#         print('%d + %d = %d' %(a,b,a+b))
#         c=random.choice([1,2,3,4,5,6])
#         d=random.choice([1,2,3,4,5,6])
#         if c+d==7:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('你输了')
#         elif c+d==a+b:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('你赢了')
# shaizi()
