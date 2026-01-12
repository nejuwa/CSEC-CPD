class ProductOfNumbers:

    def __init__(self):
        self.pref = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.pref = [1]     
        else:
            self.pref.append(self.pref[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.pref):
            return 0
        return self.pref[-1] // self.pref[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
