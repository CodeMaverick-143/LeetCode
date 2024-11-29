class Solution:
    def myPow(self, x: float, n: int) -> float:
        number = x ** n
        return float(f"{number:.5f}")