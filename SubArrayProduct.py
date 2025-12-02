class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        c=1
        ans=0
        l=0
        a=len(nums)
        if k<=1:
            return 0
        for r in range(a):
            c*=nums[r]
            while c>=k:
                c //= nums[l]
                l+=1
            ans+=r-l+1
        return ans
        
            
