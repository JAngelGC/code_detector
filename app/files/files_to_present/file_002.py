class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def merge(arr, left, right, mid):
            
            i = left
            j = mid+1
            k = left
            temp = [0] * (right+1)
            
            while i<=mid and j<=right:
                if arr[i] > arr[j]:
                    temp[k] = arr[j]
                    j += 1
                else:
                    temp[k] = arr[i]
                    i += 1
                k += 1
            
            while i<=mid:
                temp[k] = arr[i]
                i += 1
                k += 1
            
            while j<=right:
                temp[k] = arr[j]
                j += 1
                k += 1
            
            for i in range(left, right+1):
                arr[i] = temp[i]
                
            
        
        def mergeSort(arr, left, right):
            if left < right:
                mid = (left+right) // 2
                mergeSort(arr, left, mid)
                mergeSort(arr, mid+1, right)
                merge(arr, left, right, mid)
                
    
        mergeSort(nums, 0, len(nums)-1)
        # nums.sort()
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
            
            
            
            
            
            
        
        