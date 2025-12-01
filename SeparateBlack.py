class Solution:
    def minimumSteps(self, s: str) -> int:
        one = 0
        step = 0
        
        for ch in s:
            if ch == '1':
                one += 1
            else: 
                step += one
        
        return step
        
