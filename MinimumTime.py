class Solution:
    def repairCars(self, ranks, cars):
        l, r = 0, min(ranks) * cars * cars
        
        while l < r:
            m = (l + r) // 2
            if sum(int((m / r)**0.5) for r in ranks) >= cars:
                r = m
            else:
                l = m + 1
        return l
