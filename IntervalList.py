class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans=[]
        x,y = 0,0
        while x<len(firstList) and y<len(secondList):
            i,j = firstList[x]
            l,r = secondList[y]
            start = max(i,l)
            end = min(j,r)
            
            if start <= end:
                ans.append([start,end])
            if j < r:
                x += 1
            else:
                y += 1
        return ans
