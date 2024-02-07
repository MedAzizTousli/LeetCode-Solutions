class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(1,n):
            dp[0][j] = max(dp[0][j-1], prices[j]-prices[0])
        for i in range(1,n):
            for j in range(0,i+1):
                dp[i][j] = dp[i-1][j]
            for j in range(i+1,n):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], prices[j]-prices[i] + dp[i][i-2])
        return dp[-1][-1]