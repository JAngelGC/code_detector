import bisect
import copy
import gc
import itertools
from array import array
from fractions import Fraction
import heapq
import math
import operator
import os, sys
import profile
import cProfile
import random
import re
import string
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from functools import reduce, lru_cache
from io import IOBase, BytesIO
from itertools import count, groupby, accumulate, permutations, combinations_with_replacement, product
from math import gcd
from operator import xor, add
from typing import List


input = lambda: sys.stdin.readline().rstrip("\r\n")


# print = lambda d: sys.stdout.write(str(d)+"\n")
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())


# endregion


if 'AW' in os.environ.get('COMPUTERNAME', ''):
    f = open('inputs', 'r')
    def input(): return f.readline().rstrip("\r\n")

# sys.setrecursionlimit(500005)

def solve(n, nums):
    res = 0
    q = []
    for x in nums:
        heapq.heappush(q, -x)
        if q and x < -q[0]:
            res += -heapq.heapreplace(q, -x) - x
    print(res)


def main():
    for _ in range(1):
        n = read_int()
        nums = read_int_list()
        solve(n, nums)

if __name__ == "__main__":
    main()
# cProfile.run("main()")
