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

    def myPow2(self, x: float, n: int) -> float:
        def fastPow(x, n):
            if n == 0:
                return 1
            v = fastPow(x, n // 2)
            if n % 2 == 1:
                return v * v * x
            else:
                return v * v

        if n < 0:
            x = 1 / x
            n = -n

        return fastPow(x, n)

    def myPowV3GoodMem(self, x: float, n: int) -> float:
        # check if x is negative, if it is, then do the following
        if n < 0:
            x = 1/x
            n = -n
        # We solve the positive power here:
        power = 1
        current_product = x
        while n > 0:
            # if n is odd numberm, we need to time x one more time
            if n % 2:
                power = power * current_product
            current_product = current_product * current_product
            n = n//2
        return power
