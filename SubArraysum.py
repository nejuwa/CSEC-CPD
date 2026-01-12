class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1 
        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in prefix_counts:
                count += prefix_counts[prefix_sum - k]

            prefix_counts[prefix_sum] += 1

        return count
   
        
