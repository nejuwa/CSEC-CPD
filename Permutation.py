class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        slid = Counter(s1)
        wind = Counter()
        n = len(s1)
        k = len(s2)
        if n > k:
            return False
        for i in range(n):
            wind[s2[i]] += 1
        if wind == slid:
            return True
        for r in range(n,k):
            wind[s2[r]] += 1
            wind[s2[r-n]] -= 1
            if wind[s2[r-n+1]] == 0:
                del wind[s2[r-n+1]] 
            if wind == slid:
                return True
        return False

        
