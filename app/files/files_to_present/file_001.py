class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # mergeSort(nums, 0, len(nums)-1)
        nums.sort()
        triplets = []    
        numLen = len(nums)
        target = 0
        
        visPosA = []
        
        for i in range(0, numLen):
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left = i + 1
            right = numLen - 1
            # print("Here")
            
            while left < right:
                threeTarget = nums[i] + nums[right] + nums[left]
                
                if threeTarget == target:
                    newTripplet = [nums[i], nums[left], nums[right]]
                    triplets.append(newTripplet)
                    left += 1
                    while nums[left]==nums[left-1] and left<right:
                        left += 1
                    
                elif threeTarget > target:
                    right -= 1
                elif threeTarget < target:
                    left += 1
              
                    
        print(triplets)
        return triplets
            