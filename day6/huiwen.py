def isHuiwen(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

test=int(input())
print(isHuiwen(test))