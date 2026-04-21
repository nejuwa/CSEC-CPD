class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10**9 + 7
        def power_recursive(exp):
            if exp == 0:
                return 1
            if exp == 1:
                return 2
            half = power_recursive(exp // 2)
            if exp % 2 == 0:
                return (half * half) % MOD
            else:
                return (half * half * 2) % MOD
        pow2n = power_recursive(n)
        return (pow2n - 2) % MOD
