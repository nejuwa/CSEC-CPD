class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum = nums[0]
        maxx = nums[0]
        for i in range(1,len(nums)):
            presum = max(presum + nums[i], nums[i])
            maxx= max(maxx, presum)
        return maxx
