import math
n = int(input(""))
result = []

for _ in range(n):
     
    x,y = list(map(int,input("").split()))
    env = abs(x) + abs(y) -1
    lay = 1 if env == -1 else int((env*(env+1)/2)* 4) +2

    if x >= 0 and y >= 0:
        lay += x
    elif x >=0 and y <=0:
        lay += x + 2* abs(y)
    elif y<= 0:
        lay += 2*(abs(y) + abs(x)) + abs(x)
    else:
        lay += 4*(abs(y) + abs(x)) + x
    result.append(lay)


for i in result:
    print(i)