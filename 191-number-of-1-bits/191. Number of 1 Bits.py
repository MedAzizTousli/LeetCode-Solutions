class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        nb = 0
        for i in range(33):
            nb = 2 ** i
            temp = n & nb
            if temp != 0:
                res += 1
        return res