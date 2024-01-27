class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.append(0)
        amount = sum(nums)
        if amount%2 != 0:
            return False
        else:
            amount = amount//2
        dp = [False] * (amount+1)
        dp[0] = True
        mp = [{}] * (amount+1)
        mp[0] = {x:nums.count(x) for x in nums}
        # return True
        for curr in range(1, amount + 1):
            # mp[curr] = 
            for back in nums:
                # print(curr, back, mp[back])
                # mp[back] = 
                diff = curr-back
                if diff < 0:
                    continue
                # print(curr, back, diff)
                if mp[diff].get(back, 0) > 0:
                    dp[curr] = True
                    mp[curr] = mp[diff].copy()
                    mp[curr][back] -= 1
                    break
                else:
                    dp[curr] = False
                # dp[curr] = dp[curr] or dp[curr-back]
                # mp[back][back] = mp[back].get(back, 1) - 1
        # print(dp)
        # print(mp)
        return dp[amount]