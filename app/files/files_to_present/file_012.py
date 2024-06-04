class Solution:
    def threeSum(self, nums: List[int], target = 0) -> List[List[int]]:
        def findNsum(l, r, target, N, tmp, res):
            if r-l+1<N or N<2 or target < nums[l]*N or target > nums[r]*N:
                return
            if N == 2:
                while l < r:
                    sum = nums[l]+nums[r]
                    if sum==target:
                        res.append(tmp+[nums[l], nums[r]])
                        l+=1
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
                    elif sum < target:
                        l+=1
                    else:
                        r-=1
            else:
                for i in range(l, r-1):
                    if i==l or (i>l and nums[i]!=nums[i-1]):
                        findNsum(i+1, r, target-nums[i],N-1, tmp+[nums[i]], res)
        nums.sort()
        res =  []
        findNsum(0, len(nums) - 1, target, 3, [], res)
        return res
        