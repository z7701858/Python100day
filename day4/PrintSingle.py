

ty = int(input())

if ty == 1 :
    for i in range (6) :
        for j in range (i+1) :
            print("*", end='')
        print()
elif ty == 2:
    for i in range (6) :
        for j in range (6) :
            if j < 6-i-1 :
                print(" ",end="")
            else :
                print("*",end="")
        print()
else :
    for i in range(5) :
        for j in range(5-i-1) :
            print(" ",end="")
        for j in range(2 * i +1) :
            print("*",end="")
        print()