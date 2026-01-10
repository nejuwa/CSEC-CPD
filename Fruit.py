class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        l = 0
        ans = 0

        for r in range(len(fruits)):
            #basket[fruits[r]] = basket.get(fruits[r], 0) + 1

            if fruits[r] in basket:
                basket[fruits[r]] += 1
            else:
                basket[fruits[r]] = 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1

            ans = max(ans, r - l + 1)

        return ans
