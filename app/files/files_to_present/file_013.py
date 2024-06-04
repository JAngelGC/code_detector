class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        pos, neg, zer = [], [], []
        for ele in nums:
            if ele < 0:
                neg.append(ele)
            elif ele == 0:
                zer.append(0)
            else:
                pos.append(ele)
        
        POS, NEG = set(pos), set(neg)

        if len(zer) >= 1:
            for target in POS:
                if -1 * target in NEG:
                    res.add((target, 0, -1 * target))
        if len(zer) >= 3:
            res.add((0, 0, 0))
        
        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                target = neg[i] + neg[j]
                if -1*target in POS:
                    res.add(tuple(sorted([neg[i], neg[j], -1 * target])))

        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                target = pos[i] + pos[j]
                if -1 * target in NEG:
                    res.add(tuple(sorted([pos[i], pos[j], -1 * target])))
        
        return list(res)
        
        