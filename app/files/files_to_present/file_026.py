class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplet=[]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                res=nums[i]+nums[l]+nums[r]
                if res==0:
                    triplet.append([nums[i],nums[l],nums[r]])                    
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    while l<r and nums[l]==nums[l+1]:
                        l+=1                    
                    l+=1
                    r-=1
                elif res<0:
                    l+=1
                else:
                    r-=1
        return triplet