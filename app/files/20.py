n = int(input())
a = list(map(int, input().split()))
ordered = sorted(set(a))
m = len(ordered)
dp = [0] * m
for i in range(n):
    min_prev = 10 ** 18
    for j in range(m):
        min_prev = min(min_prev, dp[j])
        dp[j] = min_prev + abs(a[i] - ordered[j])
print(min(dp))
