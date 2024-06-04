class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set([])
        plus = sorted([n for n in nums if n>0])
        plus_c = set(plus)
        zero = [n for n in nums if n == 0]
        minus = sorted([n for n in nums if n<0])
        minus_c = set(minus)
        # all zero
        if len(zero)>2:
            ans.add((0,0,0))
        # plus zero minus
        if len(zero)>0:
            for n in minus:
                if -n in plus_c:
                    ans.add((n,0,-n))
        # plus minus minus
        n = len(minus)
        for i in range(n):
            for j in range(i+1,n):
                diff = -(minus[i]+minus[j])
                if diff in plus_c:
                    ans.add((minus[i],minus[j],diff))
        # plus plus minus
        n = len(plus)
        for i in range(n):
            for j in range(i+1,n):
                diff = -(plus[i]+plus[j])
                if diff in minus_c:
                    ans.add((diff,plus[i],plus[j]))
        return list(ans)