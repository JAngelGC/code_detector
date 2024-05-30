import sys
input = sys.stdin.readline

A = int(input())

res = 0

def calc(x, base):
    v = 0
    while x > 0:
        v += x % base
        x //= base

    return v

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

for i in range(2, A):
    res += calc(A, i)

d = gcd(res, A-2)

print(f'{res//d}/{(A-2)//d}')
