class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        cnt = 0
        l, r = 0, len(nums)-1
        nums.sort()
        while l<r:
            if nums[l]+nums[r] < target:
                cnt+=r-l
                l+=1
            else:
                r-=1
        return cnt


