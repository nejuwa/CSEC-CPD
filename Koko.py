class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def canEatAll(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)  
            return hours <= h

        while left < right:
            mid = (left + right) // 2
            if canEatAll(mid):
                right = mid  
            else:
                left = mid + 1 

        return left
