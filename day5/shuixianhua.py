"""
找出100-1000所有水仙花数

"""

for num in range(100,1001) :
    num_0 = num
    num_1 = num % 10
    num_2 = num //10 %10    #//	取整除 - 返回商的整数部分（向下取整）
    num_3 = num //100
    if num_0 == num_1**3 +num_2**3 +num_3**3 :
        print(num_1,num_2,num_3)
        print(num_0)