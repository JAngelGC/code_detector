class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        for i in range(len(nums)):
            first = i
            second = i + 1
            third = len(nums) - 1
            while second < third:
                curSum = nums[first] + nums[second] + nums[third]
                if curSum > 0:
                    third -= 1
                elif curSum < 0:
                    second += 1
                else:
                    triplets.add((nums[first] , nums[second] , nums[third]))
                    second += 1
        return triplets