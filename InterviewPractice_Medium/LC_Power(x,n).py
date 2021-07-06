class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        if n == -1:
            return 1/x
        else:
            if (n % 2 == 0):
                print(x, n)
                return self.myPow(x * x, n//2)
            else:
                print(x, n)
                return self.myPow(x * x, n//2) * x

            # alternatively,
            # return self.myPow(x * x, n/2) * (x if n % 2 else 1)
            # remember the difference between divisor operator /, //
