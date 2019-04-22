class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if ( len(nums) == 0):
            return 0
        count = 0
        for index in range( 0, len(nums) ):
            if nums[index] != val:
                if index != count:
                    nums[count] = nums[index]
                count += 1
        return count