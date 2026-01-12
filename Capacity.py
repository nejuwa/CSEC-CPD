class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            total = 0
            day_count = 1  
            for w in weights:
                if total + w > cap:  
                    day_count += 1
                    total = 0
                total += w
            return day_count <= days

        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            if canShip(mid):
                right = mid  
            else:
                left = mid + 1 

        return left
