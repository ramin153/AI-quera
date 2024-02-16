import math

def n_choose_m(n, m):
    return int( math.factorial(n) / (math.factorial(m) * math.factorial(n - m)))



n = int(input(""))
result = []

for i in range(0,n+1):
    coff = n_choose_m(n,i)
    coff = str(coff) if coff != 1 else ""
    x = "" if n-i == 0 else ( "x" +  ( "" if n-i == 1 else (f'^{n-i}' if n-i<= 9 else f'^{{{n-i}}}')) )
    y = "" if i == 0 else ( "y" + ("" if i == 1 else (f'^{i}' if i<= 9 else f'^{{{i}}}')))
    sent = coff + x + y
    result.append(sent)

print('+'.join(result))