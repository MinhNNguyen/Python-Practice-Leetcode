class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiff, res = sys.maxsize, 0
        for firstIndex in range( 0, len(nums) - 2):
            secondIndex, thirdIndex = firstIndex + 1, len(nums) -1
            while secondIndex < thirdIndex:
                if secondIndex > firstIndex + 1 and nums[secondIndex] == nums[secondIndex -1]:
                    secondIndex += 1
                    continue
                if thirdIndex < len(nums) -1 and nums[thirdIndex] == nums[thirdIndex + 1]:
                    thirdIndex -= 1
                    continue
                localSum = nums[firstIndex] + nums[secondIndex] + nums[thirdIndex]
                localDiff = abs(localSum - target)  
                if ( localSum == target):
                    return target
                if minDiff > localDiff:
                    minDiff = localDiff
                    res = localSum
                if (localSum > target):
                    thirdIndex -= 1
                else:
                    secondIndex += 1
        return res    