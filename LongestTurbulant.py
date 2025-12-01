class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        inc = dec = 1
        maxs = 1
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                inc = dec + 1
                dec = 1
            elif arr[i] < arr[i-1]:
                dec = inc + 1
                inc = 1
            else:
                inc = dec = 1

            maxs = max(maxs, inc, dec)
        return maxs


                    
