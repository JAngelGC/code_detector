import math
a = int(input())
s = 0
for i in range(2, a):
    tmpA = a
    while tmpA != 0:
        s = s + (tmpA % i)
        tmpA = (tmpA // i)

d = math.gcd(s, a-2)
print(f"{s//d}/{(a-2)//d}")
        
