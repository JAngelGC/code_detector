def get_sumDigit(n,base):
    sum_digits =0
    #digits = []
    while n>0:
        digit = n%base
        #digits.append(digit)
        sum_digits += digit
        n//=base
    #print(*digits[::-1],sep='')
    return sum_digits
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
n = int(input())
s=0
for i in range(2,n):
    s += get_sumDigit(n,i)
great = gcd(s,n-2)
print(s//great,'/',(n-2)//great,sep='')
