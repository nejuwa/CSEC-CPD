class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        ml = 0
        z=0
        for r in range(len(nums)):
            if nums[r] == 0 :
                z+=1
            while z>1:
                if nums[l] == 0:
                    z-=1
                l+=1
            ml = max(ml, r-l)
        return ml
        
        
        
                
        




