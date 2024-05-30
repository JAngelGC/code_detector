# LUOGU_RID: 101916896
from fractions import Fraction
n = int(input())
s = 0
for i in range(2, n):
    t = n
    while t:
        s += t % i
        t //= i
if s % (n - 2):
    print(Fraction(s, n - 2))
else:
    print(f'{s // (n - 2)}/1')