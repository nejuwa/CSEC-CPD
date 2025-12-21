class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0
        maxl= 0
        dict = defaultdict(int)

        for r in range(len(s)):
            dict[s[r]] += 1
            while dict[s[r]] > 1:
                dict[s[l]]-=1
                l+=1
            maxl= max(maxl, r-l +1)

        return maxl


