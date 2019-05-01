class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Using 3 pointers, one to denote the position of red,
        # one to denote the position of blue and one to traverse
        # the array

        red, blue, cur = 0, len(nums) - 1, 0
        while cur <= blue:
            if nums[cur] == 1:
                cur += 1
                continue
            elif nums[cur] == 0:
                if cur != red:
                    nums[cur] = nums[red]
                    nums[red] = 0
                red += 1
                cur += 1
            else:
                nums[cur] = nums[blue]
                nums[blue] = 2
                blue -= 1 
                
        
