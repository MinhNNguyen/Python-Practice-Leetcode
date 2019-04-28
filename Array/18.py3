class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for first in range (0, len(nums) - 3):
            for second in range(first + 1, len(nums) - 2):
                third, forth = second + 1, len(nums) -1
                partialSum = nums[first] + nums[second]
                while third < forth:
                    if third > second + 1 and nums[third] == nums[third - 1]:
                        third += 1
                        continue
                    if forth < len(nums) - 1 and nums[forth] == nums[forth + 1]:
                        forth -= 1
                        continue
                    if nums[third] + nums[forth] > target - partialSum:
                        forth -= 1
                    elif nums[third] + nums[forth] < target - partialSum:
                        third += 1
                    else:
                        if [nums[first], nums[second], nums[third], nums[forth]] not in res: 
                            res.append([nums[first], nums[second], nums[third], nums[forth]])
                        third += 1
                        forth -= 1
        return res