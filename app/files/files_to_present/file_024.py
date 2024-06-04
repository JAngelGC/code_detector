class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triplets_array = []
        for index in range(len(nums) - 2):
            
            # Skip positive integers
            if nums[index] > 0:
                break

            # If the number we are iterating is same as the previous number so continue it as , if we iterate again it might give duplicate triplets
            if index > 0 and nums[index] == nums[index-1]:
                continue    

            start_pointer = index + 1
            last_pointer = len(nums) - 1
            while start_pointer < last_pointer:
                
                three_sum = nums[index] + nums[start_pointer] + nums[last_pointer]

                if three_sum == 0:
                    triplets_array.append([nums[index], nums[start_pointer] ,nums[last_pointer]])
                    start_pointer += 1
                    last_pointer -= 1
                    while nums[start_pointer] == nums[start_pointer - 1] and start_pointer < last_pointer:
                        start_pointer += 1
                elif three_sum  > 0:
                    last_pointer -= 1
                else:
                    start_pointer += 1
                    
            index += 1
            
        return triplets_array