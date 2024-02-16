def list_to_1_0(seats):
   return "".join(['0' if seat else '1' for seat in seats])

n,m = list(map(int,input("").split()))

seats = [True] * n
result = []
for _ in range(m):
    s,l = list(map(int,input("").split()))
    s -=1

    for i in range(s,n-l+1):
        
        if all(seats[i:i+l]):
            for k in range(i,i+l):
                seats[k] = False
            break
    result.append(list_to_1_0(seats))

for i in result:
    print(i)