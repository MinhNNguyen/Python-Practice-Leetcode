class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find the index of the left most occurence of target
        # if not found, return len(nums)
        def findLeftMostIndex () -> int:
            lo, hi = 0, len(nums) - 1
            left = len(nums)
            while lo < hi:
                mid = round((lo + hi) / 2)
                if nums[lo] == target:
                    return lo
                if nums[mid] == target:
                    left = min(left, mid)
                    hi = mid - 1
                    continue
                if nums[hi] == target:
                    left = min(left, hi)
                    lo = mid + 1
                    continue
                if nums[mid] < target:
                    lo = mid + 1
                    continue
                else:
                    hi = mid - 1
            return left
        
        # find the index of right most occurence of target
        # if not found, return -1
        def findRightMostIndex() -> int:
            lo, hi = 0, len(nums) - 1
            right = -1
            while lo < hi:
                mid = round( (lo + hi) / 2)
                if nums[hi] == target:
                    return hi
                if nums[mid] == target:
                    right = max(right, mid)
                    lo = mid + 1
                    continue
                if nums[lo] == target:
                    right = max(right, lo)
                    hi = mid - 1
                    continue
                if nums[mid] > target:
                    hi = mid - 1 
                    continue
                else:
                    lo = mid + 1
            return right
        
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        leftBound = findLeftMostIndex()
        rightBound = findRightMostIndex()
        if leftBound == len(nums) or rightBound == - 1:
           return [-1, -1]
        else:
            return [leftBound, rightBound]
            