class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        res = []
        k=len(p)
        sliding = Counter(s[:k])
        if k> len(s):
            return res
        if target == sliding:
            res.append(0)
        for i in range(k,len(s)):
            sliding[s[i]] +=1
            sliding[s[i-k]] -=1
            if sliding == target:
                res.append(i-k+1)
        return res
            
         
                

        

