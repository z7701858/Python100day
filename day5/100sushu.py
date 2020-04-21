#输出100以内所有的素数


for i in range(1,101) :
    test = i
    #test = int(input("输入一个正整数"))
    #if test <= 1 :
        #print("输入一个正整数")
    flag=1

    for i in range(2,test) :
        if test % i ==0 :
            flag = 0
            break
    """
    if flag == 0 :
        print("no")
    else :
        print("yes")
    """
    if flag != 0 :
        print(test,end=" ")