# https://codeforces.com/problemset/problem/13/A
import math


def func_sol(raw_data):
    n = int(raw_data.split('\n')[0])
    s = 0
    for i in range(2, n):
        t = n
        while t > 0:
            s += t % i
            t //= i
    gcd = math.gcd(s, n - 2)
    return f'{s // gcd}/{(n - 2) // gcd}\n'


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
