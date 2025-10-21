class Solution:
    def isPalindrome(self, s: str) -> bool:
        all_str = [ch.lower() for ch in s if ch.isalnum()]
        j=len(all_str)-1
        
        i=0
        while i<j:
            if all_str[i] != all_str[j]:
                return False
            j-=1
            i+=1
        return True
# https://leetcode.com/problems/valid-palindrome/submissions/1807439299/
