class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        lg,ls =0,0
        cnt=0
        g.sort()
        s.sort()

        n = len(g)
        m = len(s)
        
        while lg<n and ls< m:
            if s[ls] >= g[lg]:
                cnt+=1
                ls+=1
                lg+=1
            else:
                ls+=1
        return cnt
                


