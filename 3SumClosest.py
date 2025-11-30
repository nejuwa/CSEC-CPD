class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        clos=float('inf')
        for i in range(len(nums)-2):
            l,r = i+1, len(nums)-1
            while l<r:
                s=nums[l] + nums[r] + nums[i]

                if abs(s - target) < abs(clos - target):
                    clos = s

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s   

        return clos
