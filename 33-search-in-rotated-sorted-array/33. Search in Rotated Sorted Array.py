class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        low, high = 0, len(nums)-1
        while low <= high:
            if nums[low] == target:
                res = low
                break
            if nums[high] == target:
                res = high
                break
            mid = (low+high)//2
            if nums[mid] == target:
                res = mid
                break
            if nums[mid] < target:
                if nums[high] < target:
                    if nums[mid] < nums[high]:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    low = mid + 1
            else:
                if nums[high] > target:
                    if nums[mid] < nums[high]:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    high = mid - 1
        return res