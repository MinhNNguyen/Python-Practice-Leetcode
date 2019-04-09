class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index in range( len(nums) ):
            complement = target - nums[index]
            if complement in dict:
                return [dict.get(complement), index]
            dict[nums[index]] = index
        return [-1, -1]
        