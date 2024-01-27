class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 5000
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            res = min(res, nums[mid])
            if nums[mid] < nums[high]:
                high = mid - 1
            else:
                low = mid + 1
        return res