# Short solution

class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        i, j = 0, 1 # nums[i:j] can be visited in cnt jumps
        for cnt in range(len(nums)):
            i, j = j, max(k+nums[k]+1 for k in range(i, j))
            if j >= len(nums):
                return cnt + 1

# Keep track of the minimum last index not searched and max index can be reach with every jump

class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        lastMaxJump, currentMaxJump = 0, nums[0]
        if (currentMaxJump >= len(nums) - 1):
            return 1
        count = 1
        while True:
            nextMaxJump = max(k + nums[k] for k in range(lastMaxJump + 1, currentMaxJump + 1))
            if nextMaxJump >= len(nums) - 1:
                return count + 1
            lastMaxJump = currentMaxJump
            currentMaxJump = nextMaxJump
            count += 1
        