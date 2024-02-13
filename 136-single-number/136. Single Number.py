class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = 0
        for i in nums:
            seen ^= i
        return seen