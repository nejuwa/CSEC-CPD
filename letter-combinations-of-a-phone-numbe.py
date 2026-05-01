class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        res=[]
        def backtrack(ind, comb):
            if ind == len(digits):
                res.append(comb)
                return
            pon = digits[ind]
            letters = phone[pon]
            for leter in letters:
                backtrack(ind +1, comb + leter)
        backtrack(0, "")
        return res

