class Solution:
    def __init__(self):
        self.best = 1
        self.this = 0

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        visited = set()
        dp = [[0 for j in range(m)] for i in range(n)]
        def dfs(i, j, curr):
            if i < 0 or j < 0 or i >= n or j >= m:
                return None
            if (i,j) in visited:
                return None
            if dp[i][j] != 0:
                self.this = max(curr+dp[i][j]-1, self.this)
                return None
            # dp[x][y] = max(dp[x][y], curr)
            # self.best = max(curr, self.best)
            self.this = max(curr, self.this)
            visited.add((i, j))
            # dp[i][j] += 1
            if i+1 < n and matrix[i+1][j] > matrix[i][j]:
                dfs(i+1, j, curr+1)
            if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                dfs(i-1, j, curr+1)
            if j+1 < m and matrix[i][j+1] > matrix[i][j]:
                dfs(i, j+1, curr+1)
            if j+1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                dfs(i, j-1, curr+1)
            # dp[i][j]
            visited.remove((i, j))
            # dp[x][y] = 
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                self.this = 0
                dfs(i, j, 1)
                dp[i][j] = self.this
        res = 1
        for i in dp:
            res = max(res, max(i))
            # print(i)
        return res