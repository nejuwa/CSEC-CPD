class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r =1, len(skill)-2
        cnt = skill[0]*skill[r+1]
        total = skill[0]+skill[r+1]
        while l<r:
            if total == skill[l]+skill[r]:
                cnt += skill[l]*skill[r]
                l+=1
                r-=1
            else:
                return -1
                
        return cnt
