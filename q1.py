n = int(input(""))

for i in range(0,n-1):
    output = ['.']*(2*n-1)
    output[n-i-1] = 'D'     
    output[n+i-1] = 'D'
    print("".join(output))

print('D.'*(n-1)+'D')