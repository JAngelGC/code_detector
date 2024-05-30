# LUOGU_RID: 100463992
n=int(input())
k=0
z=n
for i in range(2,n):
    while n!=0:
        k+=n%i
        n=n//i
    n=z
a=max(k,n-2)
b=min(k,n-2)
n=a%b
while n!=0:
    a=b
    b=n
    n=a%b
print(int(k/b),end='/')
print(int((z-2)/b))