class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        freqs = dict()
        for x in nums:
            if x not in freqs:
                freqs[x] = 0
            freqs[x] += 1
        
        ans = []

        # Triples with all three members equal: just (0, 0, 0)
        if 0 in freqs and freqs[0] >= 3:
            ans.append([0,0,0])
        # Triples with exactly 2 members equal: (x, x, -2x) where x != 0
        for x in freqs:
            if x == 0: continue
            if freqs[x] >= 2 and -2*x in freqs:
                ans.append([x, x, -2*x])
        # Triples with all three members distinct
        cnums = sorted(freqs.keys())
        n = len(cnums)
        for i in range(n):
            if cnums[i] > 0: break
            for j in range(i+1, n):
                comp = -cnums[i]-cnums[j]
                if comp <= cnums[j]: break
                if comp in freqs:
                    ans.append([cnums[i], cnums[j], comp])
        
        return ans