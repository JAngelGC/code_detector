import sys

input = sys.stdin.readline
n, m = map(int, input().split())
p = list(map(int, input().split()))
size = 320
block = [i // size for i in range(n)]
par, cnt = [0] * n, [0] * n
for i in range(n - 1, -1, -1):
    setelah = i + p[i]
    if setelah >= n:
        par[i] = i + n
        cnt[i] = 1
    elif block[setelah] == block[i]:
        par[i] = par[setelah]
        cnt[i] = cnt[setelah] + 1
    else:
        par[i] = setelah
        cnt[i] = 1
ans = []
for _ in range(m):
    s = input().strip()
    if s[0] == '0':
        Z, a, b = s.split()
        a = int(a) - 1
        b = int(b)
        p[a] = b
        i = a
        while i >= 0 and block[i] == block[a]:
            setelah = i + p[i]
            if setelah >= n:
                par[i] = i + n
                cnt[i] = 1
            elif block[i] == block[setelah]:
                par[i] = par[setelah]
                cnt[i] = cnt[setelah] + 1
            else:
                par[i] = setelah
                cnt[i] = 1
            i -= 1
    else:
        Z, a = s.split()
        a = int(a) - 1
        now = 0
        while a < n:
            now += cnt[a]
            a = par[a]
        ans.append(str(a - n + 1) + ' ' + str(now))
print('\n'.join(ans))
