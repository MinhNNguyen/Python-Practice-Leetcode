class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[-1 for i in range(n)] for j in range(n)]
        count = 1
        lo, hi = 0, n - 1
        while lo <= hi:
            if lo == hi:
                res[lo][hi] = count
                return res
            for index in range(lo, hi):
                res[lo][index] = count
                count += 1
            for index in range(lo, hi):
                res[index][hi] = count
                count += 1
            for index in range(hi, lo, -1):
                res[hi][index] = count
                count += 1
            for index in range(hi, lo, -1):
                res[index][lo] = count
                count += 1
            lo += 1
            hi -= 1
        return res
                
        
        