class Solution:
    """
        if n is even:
            x ** n = (x ** n // 2) ** 2
        else:
            x ** n = (x ** n // 2) ** 2 * n
    """

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        return self.fast_pow(x, n)

    def fast_pow(self, x, n):
        if not n:
            return 1.0

        half = self.fast_pow(x, n // 2)
        if n % 2:
            return half * half * x
        else:
            return half * half
