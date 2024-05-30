import sys
# sys.setrecursionlimit(int(1e9))
# import random
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce
# from itertools import accumulate,product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
# from bisect import bisect_left,bisect_right
# from sortedcontainers import SortedList
# input = sys.stdin.buffer.readline
# import re
input = lambda:sys.stdin.readline().rstrip("\r\n")
def mp():return list(map(int,input().split()))
def it():return int(input())
# import math

MOD = int(1e9 + 7)
INF = int(1e18)

def solve():
    n=it()
    nums=mp()
    ans,pq=0,[]
    for num in nums:
        if pq and -pq[0]>num:
            ans+=-heappop(pq)-num
            heappush(pq,-num)  # 使小于当前横坐标值的线段保持其之前的斜率 rank 值
        heappush(pq,-num)  # 所有斜率都减一
    print(ans)

    return

if __name__ == '__main__':

    # t=it()
    # for _ in range(t):
    #     solve()

    # n=it()
    # n,m,i=mp()
    # n,m=mp()
    solve()