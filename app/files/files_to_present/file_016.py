class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        li=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                l=i+1
                r=len(nums)-1
                while l<r:
                    sumx=nums[i]+nums[l]+nums[r]
                    if(sumx<0):
                        l+=1
                    elif(sumx>0):
                        r-=1
                    else:
                        triplet=[nums[i],nums[l],nums[r]]
                        li.append(triplet)
                        while r>l and nums[r]==triplet[-1]:
                            r-=1
                        while r>l and nums[l]==triplet[1]:
                            l+=1
        return li

        