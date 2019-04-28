class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hmap = []
        res = 1
        
        for index in range( 0, len(nums) ):
            hmap.append(nums[index])
        
        while res in hmap:
            res += 1
        
        return res

# Second solution run munch faster
class Solution:
def firstMissingPositive(self, nums: List[int]) -> int:
    n = len(nums)
    # Traverse first time to mark every negative number into n + 1
    for i in range(n):
        if nums[i] <= 0: nums[i] = len(nums) + 1
    # Traverse second time to make sure the value of every index that appears in the
    # number array will be marked zeo
    for i in range(n):
        if abs(nums[i]) <= n:
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
    #return the index of first number that has the positive value, otherwise return n + 1
    for i in range(n):
        if nums[i] > 0: return i + 1
    return n + 1




            
        
        
        
            
        