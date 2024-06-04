
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        target = 0
        size = len(nums) - 1
        triplets = []

        for i in range(size):

            if i>0 and nums[i]==nums[i-1]:
                continue # do not use the same same value

            fixedVal = nums[i] # become Two sum problem

            left = i + 1
            right = size
            while left < right:
                generatedVal = nums[left] + nums[right] + fixedVal

                if generatedVal > target:
                    right -= 1
                elif generatedVal < target:
                    left += 1
                else: # generatedVal == target
                    triplets.append([nums[left], nums[right], fixedVal])
                    left += 1
                    while nums[left] == nums[left-1] and left<right:
                        left += 1

        return triplets




