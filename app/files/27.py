from math import log,ceil,gcd
n = int(input())
a = 0
for i in range(2,n):
    m = n
    while m:
        m,r = divmod(m,i)
        a += r
g = gcd(a,n-2)
print(f"{a//g}/{(n-2)//g}")