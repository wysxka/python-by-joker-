# 01 定级
# score = int(input('亲，请输入成绩:>>'))
# def grade(g):
#         print ("你的成绩等级为： %s " % g)
# if 90 <= score <= 100:
#         grade('A')
# elif score >= 80:
#         grade('B')
# elif score >= 70:
#         grade('C')
# elif score >=  60:
#         grade('D')
# else:
#         grade('F')


# 02 逆序读取的数字
# def main():
#     list =[1,2,3,4,5,6,7,8,9]
#     list_n =[]
#     list_n =list[::-1]
#     print(list_n)
# if __name__ == "__main__":
#     main()


# 03 统计数字个数
# print("Enter the numbers between 1 and 100:")
# enterList=[] #记录输入的元素
# while 1:
#     a = int(input(">>>"))  #将输入转换为int型
#     if a == 0:
#         print ("Your input:",enterList)
#         break  #结束输入
#     if a<1 or a>100:  #限制只允许输入1到100之间的数
#         print("Error!Please enter the numbers between 1 and 100!")
#     else:
#         enterList.append(a)
# listVisited=[]  #保存列表中已经处理过的元素值，避免相同的值处理多次
# for a in enterList:
#     if a in listVisited: #已经处理过a，跳过此次循环
#         break
#     if enterList.count(a)>1:
#         print("The number",a,"occurs",enterList.count(a),"times!")
#     if enterList.count(a)==1:
#         print("The number",a,"occurs",enterList.count(a), "time!")
#     listVisited.append(a) #处理完a，把a保存到这个列表中，以便下次跳过a的值

# 04 分析成绩
# def average(list):
#    pinjun = sum(list)/(len(list)*1.0)
#    return pinjun
# num1 = 0
# num2 = 0
# def fenshu(list_):
#     pinjun = average(list_)
#     for i in range(len(list_)):
#         
#         global num1
#         global num2
#         if list_[i] > pinjun: 
#             num1 += 1
#         elif list_[i] < pinjun:
#             num2 += 1
#         else:
#             pass
#     print(num1)
#     print(num2)
#     print(pinjun)
# fenshu([2,4,2,4,8])S

# 05 统计单个数字
#import numpy
#def suiji():
#    a = numpy.random.choice(range(1000))
#    return a
#for i in range(1000):
#    str1 = [suiji(),suiji(),suiji(),suiji(),suiji(),suiji(),suiji(),suiji(),suiji(),suiji()]
#    print(str1)


# 06 找出最小元素的下标

# 07 随机数字选择器

# 08 消除重复
# lst=list(map(int,input('Please enter a list of number:').split(' ')))
# def eliminateDupLicates(lst):
# set1=set(lst)
# for i in set1:
# print(i,end=' ')  
# if __name__ == '__main__':
# eliminateDupLicates(lst)

# 09 有序吗
# 10 冒泡排序
# 11 模拟:优惠券收集问题 
# 12 模式识别：四个连续的相同的数
# 001 检测SSN
# 002 检测子串
# 003 检测密码
# 004 统计字符串中的字母个数
# 005 手机键盘
# 006 反向字符串
# 007 金融:信用卡号合法性
# 008 商业：检测ISBN-13
