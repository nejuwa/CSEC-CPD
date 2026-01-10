class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        maxf = 0
        ans = 0

        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            count[idx] += 1

            maxf = max(maxf, count[idx])

            while (r - l + 1) - maxf > k:
                left_id = ord(s[l]) - ord('A')
                count[left_id] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
