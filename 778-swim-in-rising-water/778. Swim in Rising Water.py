class Solution:
    def __init__(self):
        self.res = -1

    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        n = len(grid)
        q = []
        heapq.heappush(q, (grid[0][0], 0, 0))
        while q:
            t, i, j = heapq.heappop(q)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            self.res = max(self.res, t)
            if i == n-1 and j == n-1:
                return self.res
            if i+1 < n: heapq.heappush(q, (grid[i+1][j], i+1, j))
            if i-1 >= 0: heapq.heappush(q, (grid[i-1][j], i-1, j)) 
            if j+1 < n: heapq.heappush(q, (grid[i][j+1], i, j+1))
            if j-1 >= 0: heapq.heappush(q, (grid[i][j-1], i, j-1))
