class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            b= i + 1
            r= n - 1   

            while b < r:
                s = nums[i] + nums[b] + nums[r]

                if s == 0:
                    res.append([nums[i], nums[b], nums[r]])
                    b += 1
                    r -= 1
                    while b < r and nums[b] == nums[b - 1]:
                        b += 1
                elif s < 0:
                    b += 1
                else:
                    r -= 1

        return res
