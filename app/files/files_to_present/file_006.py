from typing import List

class Solution:
    def findTriplets(self, arr: List[int]) -> List[List[int]]:
        result = []
        arr.sort()
        
        for idx in range(len(arr)):
            if idx > 0 and arr[idx] == arr[idx - 1]:
                continue
            
            left, right = idx + 1, len(arr) - 1
            
            while left < right:
                total = arr[idx] + arr[left] + arr[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([arr[idx], arr[left], arr[right]])
                    left += 1
                    
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
      
