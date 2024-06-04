# Brute Force
# TC: O(n*n*n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arrLength = len(nums)

        ans = []


        for i_idx in range(0, arrLength - 2):
            for j_idx in range(i_idx + 1, arrLength - 1):
                for k_idx in range(j_idx + 1, arrLength):
                    if nums[i_idx] + nums[j_idx] + nums[k_idx] == 0:
                        # Sort the triplet and add it to the result if not already present
                        triplet = sorted([nums[i_idx], nums[j_idx], nums[k_idx]])
                        
                        if triplet not in ans:
                            ans.append(triplet)

        return ans