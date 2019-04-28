import copy

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def findNextNumber(existingNums: List[int], res: List[List[int]], rem: int, start: int) -> None:
            if rem == 0:
                res.append(copy.deepcopy(existingNums))
                return
            for index in range( start, len(candidates) ):
                if rem >= candidates[index]:
                    existingNums.append(candidates[index])
                    findNextNumber(existingNums, res, rem - candidates[index], index)
                    existingNums.pop()
        
        res = []
        existingNums= []
        findNextNumber(existingNums, res, target, 0)
        return res

                    
        
                
            