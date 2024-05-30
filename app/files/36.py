import math
a = int(input())
n = 0
for i in range(2,a):
    x=a
    while x: 
        n+=x%i
        x//=i
 
b=math.gcd(n,a-2)
print(str(n//b)+'/'+str((a-2)//b))