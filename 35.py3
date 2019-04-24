import math

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = math.floor( (lo + hi) / 2)
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

        # Case when lo == hi
        return lo if target <= nums[lo] else hi + 1