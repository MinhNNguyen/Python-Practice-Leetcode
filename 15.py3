class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for firstIndex in range ( 0, len(nums) - 2 ):
            if (firstIndex > 0 and nums[firstIndex] == nums[firstIndex - 1]):
                continue
            firstNum = nums[firstIndex]
            if firstNum > 0:
                return res
            sum = 0 - firstNum
            secondIndex, thirdIndex = firstIndex + 1, len(nums) - 1
            while secondIndex < thirdIndex:
                if secondIndex > firstIndex + 1 and nums[secondIndex] == nums[secondIndex - 1]:
                    secondIndex += 1
                    continue
                if thirdIndex < len(nums) - 1 and nums[thirdIndex] == nums[thirdIndex + 1]:
                    thirdIndex -= 1
                    continue
                if nums[secondIndex] + nums[thirdIndex] > sum:
                    thirdIndex -= 1
                elif nums[secondIndex] + nums[thirdIndex] < sum:
                    secondIndex += 1
                else:
                    res.append([firstNum, nums[secondIndex], nums[thirdIndex]])
                    secondIndex += 1
                    thirdIndex -= 1
        return res
                
            
            