class Solution:
    def myPow(self, x: float, n: int) -> float:
        def Pow(x, n):
            if n == 0:
                return 1
            res = Pow(x, n >> 1)
            if n % 2 == 1:
                res = res * res * x
            else:
                res = res * res
            return res
        if n >= 0:
            return Pow(x, n)
        else:
            return 1 / Pow(x, abs(n))