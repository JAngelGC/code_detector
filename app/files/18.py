N=int(input())
A=list(map(int,input().split()))

S=sorted(set(A))
DP=[0]*len(S)

for a in A:
    NDP=[0]*len(S)

    MIN=1<<60

    for i in range(len(S)):
        MIN=min(MIN,DP[i])
        x=S[i]

        NDP[i]=abs(a-x)+MIN

    DP=NDP

print(min(DP))
