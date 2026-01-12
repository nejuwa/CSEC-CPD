class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre_sum = 0
        res= []
        for i in nums:
            pre_sum += i
            res.append(pre_sum)
        return res
