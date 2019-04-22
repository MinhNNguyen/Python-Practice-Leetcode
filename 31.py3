class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return
        for pos in range( len(nums) - 1, 0, -1):
            if nums[pos] > nums[pos - 1]:
                # find the smallest number that is bigger than pos - 1 to swap with it
                minBigger = nums[pos]
                minIndex = pos
                for index in range(pos, len(nums) ):
                    if nums[index] > nums[pos -1 ] and nums[index] <= minBigger:
                        minIndex = index
                        minBigger= nums[index]
                
                #swap
                temp = nums[pos - 1]
                nums[pos - 1] = minBigger
                nums[minIndex] = temp
                
                # reverse the order from pos to the end of the list
                left = pos
                right = len(nums) - 1
                while left < right:
                    temp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = temp
                    left += 1
                    right -= 1
                return
        nums.reverse()