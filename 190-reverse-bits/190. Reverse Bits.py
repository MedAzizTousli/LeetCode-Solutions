class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        nb = 0
        for i in range(33):
            nb = 2 ** i
            tmp = n & nb
            if tmp != 0:
                res += 2 ** (31-i)
        return res