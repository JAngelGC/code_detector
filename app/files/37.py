import math
a=int(input());

ans=0;
for b in range(2,a):
    tmp=a;
    while tmp>=b:
        ans+=(tmp%b);
        tmp//=b;
    ans+=tmp;

num=a-2
gcd=math.gcd(ans,num);
print(str(ans//gcd)+'/'+str(num//gcd));
    
