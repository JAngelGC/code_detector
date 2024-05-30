import sys

input = sys.stdin.readline
n, m = map(int, input().split())
p = list(map(int, input().split()))
LENGTH = 320
block = [i // LENGTH for i in range(n)]
lompat = [0] * n
akhir = [0] * n
for i in range(n - 1, -1, -1):
    next = i + p[i]
    if next >= n:
        akhir[i] = i + n
        lompat[i] = 1
    elif block[i] != block[next]:
        lompat[i] = 1
        akhir[i] = next
    else:
        lompat[i] = lompat[next] + 1
        akhir[i] = akhir[next]
ans = []
for _ in range(m):
    s = input().strip()
    if s[0] == '0':
        a, b, c = s.split()
        b = int(b) - 1
        c = int(c)
        p[b] = c
        i = b
        while i >= 0 and block[i] == block[b]:
            next = i + p[i]
            if next >= n:
                akhir[i] = i + n
                lompat[i] = 1
            elif block[i] != block[next]:
                lompat[i] = 1
                akhir[i] = next
            else:
                lompat[i] = lompat[next] + 1
                akhir[i] = akhir[next]
            i -= 1
    else:
        a, b = s.split()
        sekarang = int(b) - 1
        total = 0
        while sekarang < n:
            total += lompat[sekarang]
            sekarang = akhir[sekarang]
        ans.append(str(sekarang - n + 1) + ' ' + str(total))
print('\n'.join(ans))
