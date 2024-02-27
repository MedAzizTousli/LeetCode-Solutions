class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[0]
        possible = True
        for i in range(1, len(nums)):
            if curr == 0:
                possible = False
            curr = max(nums[i], curr-1)
        return possible