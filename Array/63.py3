class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if (m == 0 or n == 0):
            return 0
        paths = [[0 for i in range(m + 1)] for j in range(n + 1)]
        paths[0][1] = 1
        for horizontalPos in range(1, m + 1):
            for verticalPos in range(1, n + 1):
                if obstacleGrid[verticalPos - 1][horizontalPos - 1] == 0:
                    paths[verticalPos][horizontalPos] = paths[verticalPos - 1][horizontalPos] + paths[verticalPos][horizontalPos - 1]
        return paths[n][m]