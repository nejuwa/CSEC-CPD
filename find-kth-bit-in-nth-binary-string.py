class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def build_string(s):
            if s == "0":
                return "0"
        def find_bit(n, k):
            if n == 1:
                return "0"
            length = (1 << (n - 1)) - 1  # 2^(n-1) - 1
            if k == length + 1:
                return "1"
            elif k <= length:
                return find_bit(n - 1, k)
            else:
                pos_in_original = (1 << n) - k  # 2^n - k
                bit = find_bit(n - 1, pos_in_original)
                return "1" if bit == "0" else "0"
        
        return find_bit(n, k)
      

                




