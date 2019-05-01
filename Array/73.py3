class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        height, width = len(matrix), len(matrix[0])
        cols = [False] * height
        rows = [False] * width
        
        for yCoor in range(len(cols)):
            for xCoor in range(len(rows)):
                if matrix[yCoor][xCoor] == 0:
                    cols[yCoor] = True
                    rows[xCoor] = True
        
        for yCoor in range(len(cols)):
            for xCoor in range(len(rows)):
                if cols[yCoor] or rows[xCoor]:
                    matrix[yCoor][xCoor] = 0
                    
        
        
        