class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        cnt = -1
        l, r = 0, 0
        while l<len(nums1) and r<len(nums2):
            if nums1[l] == nums2[r]:
                cnt = nums1[l]
                break
            elif nums1[l] < nums2[r]:
                l+=1
            else:
                r+=1
        return cnt
