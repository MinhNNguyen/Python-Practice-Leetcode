class Solution:

    # Original solution using while loop
    def removeDuplicates(self, nums: List[int]) -> int:
        if ( len(nums) < 2):
            return len(nums)
        slow, fast = 1, 1
        count = 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                count += 1
                if slow != fast:
                    nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return count

    # Attemp to write shorter and faster using for loop
    def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    count = 0
    for pointer in range( 1, len(nums)):
        if nums[pointer] != nums[pointer - 1]:
            count += 1
            nums[count] = nums[pointer]
    return count + 1