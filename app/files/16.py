
from bisect import insort
def min_steps_N(arr):
    pri_q = []
    ans = 0
    for n in arr:
        if pri_q:
            if pri_q[-1] > n:
                ans += pri_q[-1] - n
                pri_q.pop()
                insort(pri_q, n)
        insort(pri_q, n)
    return ans

if __name__ == '__main__':
    N = input()
    arr = list(map(int, input().split(' ')))
    print(min_steps_N(arr))
