class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length = len(triangle)
        dp = triangle[length - 1]
        for floor in range(length - 2, -1, -1):
            for pos in range(len(triangle[floor])):
                dp[pos] = min( dp[pos], dp[pos + 1] ) + triangle[floor][pos]
        return dp[0]
            
        