"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

"""

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a+b>c and a+c>b and b+c>a :
    if a+b<c and a+c<b and b+c<a :
        l = a+b+c
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print("l = ",l)
        print("s = ",s)
    else :
        print("not a single!")
else :
    print("not a single!")