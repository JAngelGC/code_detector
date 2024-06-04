class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #First of all we have to sort the nums
        nums=sorted(nums)
        res=set()
        for n in range(len(nums)):
            #Hold the one digit that is n
            i=n+1
            #i start with range n+1 onwards and j comes with end of the nums
            j=len(nums)-1
            while i<j:
                #The i will find the one digit and j will find the another digits which sum is equal to zero
                summ=nums[n]+nums[i]+nums[j]
                if summ==0:
                    #Then we have to add thse into the set
                    res.add((nums[n],nums[i],nums[j]))
                    i=i+1
                    j=j-1
                    #The three sum is equal to zero then move the two pointers.
                elif summ>0:
                    #if sum is less than zero we have to decrement the j because the nums is sorted right.
                    j=j-1
                elif summ<0:
                    #As well as i will have to increment
                    i=i+1
        #Finallt return the re
        return res