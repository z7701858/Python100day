def maxgongyue(x,y):
    (x,y)=(y,x) if x>y else (x,y)
    for i in range(x,0,-1):
        if x%i==0 and y%i==0:
            return i

def mingong(x,y):
    return x*y//maxgongyue(x,y)

a=int(input())
b=int(input())
print(maxgongyue(a,b))
print(mingong(a,b))