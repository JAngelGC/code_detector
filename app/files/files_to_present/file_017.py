class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        n = len(nums)
        nums.sort()

        def sum2(i, target):
            low = i+1
            high = n-1
            while low < high:
                s = nums[low] + nums[high]
                if s > target:
                    high -= 1
                elif s < target:
                    low += 1
                else:
                    triplets.append([nums[i], nums[low], nums[high]])

                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low-1]:
                        low += 1
                        
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            complement = -nums[i]
            sum2(i, complement)
        
        return triplets