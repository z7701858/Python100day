"""
输入一个正整数判断它是不是素数

素数指的是只能被1和自身整除的大于1的整数。
"""



test = int(input("输入一个正整数"))
if test <= 1 :
    print("输入一个正整数")

flag=1

for i in range(2,test) :
    if test % i ==0 :
        flag = 0
        break

if flag == 0 :
    print("no")
else :
    print("yes")