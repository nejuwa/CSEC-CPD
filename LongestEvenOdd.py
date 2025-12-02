class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        odd=eve=0
        c=0
        for r in nums:
            if r > threshold:
                eve=odd=0
                continue
            if r%2==0 :
                eve=odd+1
                odd=0
            else:
                if eve>0:
                    odd=eve+1
                else:
                    odd=0
                eve=0
            c=max(c,eve,odd)
        return c
        

