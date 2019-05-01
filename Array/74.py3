class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchNumber( col: int) -> bool:
            lo, hi = 0, width - 1
            while lo <= hi:
                mid = round((lo + hi) / 2)
                if target == matrix[col][mid]:
                    return True
                elif target < matrix[col][mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return False
        
        height = len(matrix)
        width = len(matrix[0]) if height > 0 else 0
        if height == 0 or width == 0:
            return False
        lo, hi = 0, height - 1
        while lo <= hi:
            if target > matrix[hi][width - 1] or target < matrix[lo][0]:
                return False
            mid = round((lo + hi) / 2)
            if matrix[mid][0] <= target <= matrix[mid][width - 1]:
                return searchNumber(mid)
            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
        
        
        
        