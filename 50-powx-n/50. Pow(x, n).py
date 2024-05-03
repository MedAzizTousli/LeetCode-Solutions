class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1
        if n < 0:
            x = 1/x
            n = -n
        mp = {}
        def dfs(n):
            if n == 1:
                return x
            if n == 0:
                return 0
            if n in mp:
                return mp[n]
            if n % 2 == 0:
                res = dfs(n//2)
                return res * res
            else:
                return dfs(n//2)*dfs(n-n//2)
        return dfs(n)
