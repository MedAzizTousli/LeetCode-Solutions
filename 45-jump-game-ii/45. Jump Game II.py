class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        l = []
        heapq.heapify(l)
        heapq.heappush(l, [0, 0])
        for i in range(1, len(nums)):
            while l[0][1] + nums[l[0][1]] < i:
                heapq.heappop(l)
            best = l[0][0]
            idx = l[0][1]
            dp[i] = best + 1
            if nums[i] != 0:
                heapq.heappush(l, [dp[i], i])
        return dp[-1]
