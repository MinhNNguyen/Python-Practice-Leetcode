class Solution:
    def nSum (self, nums: List[int], target: int, N: int) -> List[List[int]]:
        nums.sort()
        results = []
        findNSum(0, len(nums) - 1, N, target, [], results)
        return results

        def findNSum(left, right, N, target, result, results): 
            # early termination
            if right - left + 1 < N or N < 2 or target < nums[left] * N or target > nums[right] * N:
                return
            if N == 2:
                while left < right:
                    if left + right < target:
                        left += 1
                    elif left + right > target:
                        right -= 1
                    else:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
            else: 
            # running recursively
                for i in range(left, right + 1):
                    if i == left or ( i > left and nums[i - 1] != nums[i]):
                        findNSum(i + 1, right, target - nums[i], N - 1, result + [nums[i]], results)
            




