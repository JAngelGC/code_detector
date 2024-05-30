import math
a=int(input())
r=0
for b in range(2,a):
  c=a
  while c:r+=c%b;c//=b
a-=2
d=math.gcd(r,a)
print(f'{r//d}/{a//d}')