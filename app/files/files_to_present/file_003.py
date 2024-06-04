class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Returns index of x in arr if present, else -1
        def binary_search(arr, low, high, x):
            if high >= low:
                mid = (high + low) // 2

                if arr[mid] == x:
                    return mid

                elif arr[mid] > x:
                    return binary_search(arr, low, mid - 1, x)

                else:
                    return binary_search(arr, mid + 1, high, x)
            else:
                return -1

        
        
        nums.sort()
        target = 0
        
        triplets = []
        
        for i in range(0, len(nums) - 2):
            
            fix1 = nums[i]
            fix2 = nums[i+1]
            
            print(fix1, fix2)
            
            sumFxs = (fix1 + fix2) * -1
            # print("sumFXS: ", sumFxs)
            
            ansBS = binary_search(nums, i, len(nums)-1, sumFxs)
            # print("ansBS: ", ansBS)
            
            if ansBS != -1:
                newTrip = [fix1, fix2, nums[ansBS]]
                newTrip.sort()
                triplets.append(newTrip)
                
        
        # remove duplicated from list 
        result = [] 
        for i in triplets: 
            if i not in result: 
                result.append(i) 
        print(result)
        return result
        
        
        