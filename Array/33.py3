class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def partialSearch(nums: List[int], left: int, right: int, target: int) -> int:
            # check if left is still smaller than right
            if left > right:
                return -1

            # check if target is equal to any bound
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            mid = round( (left + right) / 2 )
            if nums[mid] == target:
                return mid

            # check if this part of the array is sorted array or rotated array, and specify case for each
            if nums[right] > nums[left]:
                if target > nums[right] or target < nums[left]:
                    return -1
                elif target < nums[mid]:
                    return partialSearch(nums, left + 1, mid - 1, target)
                else:
                    return partialSearch(nums, mid + 1, right - 1, target)
            else:
                return max(partialSearch(nums, left + 1, mid - 1, target), partialSearch(nums, mid + 1, right - 1, target))
        
        return partialSearch(nums, 0, len(nums) - 1, target)
                
                
            
                
            