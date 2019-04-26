class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hmap = []
        res = 1
        
        for index in range( 0, len(nums) ):
            hmap.append(nums[index])
        
        while res in hmap:
            res += 1
        
        return res
            
        
        
        
            
        