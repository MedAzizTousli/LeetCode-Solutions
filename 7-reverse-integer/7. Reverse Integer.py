class Solution:
    def reverse(self, x: int) -> int:
        sign = 0
        if x != 0:
            sign = int(x/abs(x))
        x = abs(x)
        res = 0
        while x != 0:
            nb = x % 10
            x = x // 10
            res = res * 10 + nb
        if res > 2**31-1 or -res < -2**31:
            return 0  
        return sign * res