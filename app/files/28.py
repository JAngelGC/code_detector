from math import gcd
def sanoq(n,x):
    s=0
    while n:
        s, n = s+n%x, n//x
    return s
a=int(input())
j=0
for x in range(2,a):
    j+=sanoq(a,x)
g=gcd(j,a-2)
print(f"{j//g}/{(a-2)//g}")