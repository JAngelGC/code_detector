class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to use two-pointer technique
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements to avoid duplicate triplets
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    # Skip duplicate elements for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return triplets