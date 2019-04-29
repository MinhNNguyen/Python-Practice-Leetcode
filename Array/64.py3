class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        if (height == 0 or width == 0):
            return 0
        minPaths = [[ 0 for x in range(width + 1)] for y in range(height + 1)]
        minPaths[0] = [sys.maxsize] * (width + 1) 
        for index in range(height + 1):
            minPaths[index][0] = sys.maxsize
        minPaths[0][1] = 0
        for verticalPos in range(1, height + 1):
            for horizontalPos in range(1, width + 1):
                minPaths[verticalPos][horizontalPos] = min( minPaths[verticalPos - 1][horizontalPos], minPaths[verticalPos][horizontalPos - 1]) + grid[verticalPos - 1][horizontalPos - 1]
        return minPaths[height][width]