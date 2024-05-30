import heapq
input()
ans=0
a=[]
inf=10**9
for x in map(int,input().split()):
    x=inf-x
    heapq.heappush(a,x)
    ans+=a[0]-x
    heapq.heappop(a)
    heapq.heappush(a,x)
print(-ans)
