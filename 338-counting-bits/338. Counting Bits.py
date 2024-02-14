class Solution:
    def countBits(self, n: int) -> List[int]:
        def calculate(n):
            res = 0
            nb = 0
            for i in range(33):
                nb = 2 ** i
                temp = n & nb
                if temp != 0:
                    res += 1
            return res
        l = []
        for i in range(n+1):
            l.append(calculate(i))
        return l