class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        remainder = defaultdict(int)
        remainder[0] = 1   
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            rem = prefix_sum % k   

            result += remainder[rem]
            
            remainder[rem] += 1

        return result
