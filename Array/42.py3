''' To approach this problem, we can traverse through an array to find the highest column
    in all of the array or the list of highest column.The rest of easy, saying if we have
     3 highest columns with the same height, we can easily calculate the water trapped
      among those heightest columns. Otherwise, we need to calculate the water trapped
       from column 0 to the first highest colmn, and from last hight column to the last
        column being provided. '''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        maxHeight = 0
        maxCol = []
        for index in range(len(height)):
            if height[index] > maxHeight:
                maxHeight = height[index]
                maxCol = [index]
            elif height[index] == maxHeight:
                maxCol.append(index)
        
        # calculate trapping water between index 0 and maxCol[0]
        localMax = 0
        waterTrapped = 0
        for index in range(0, maxCol[0]):
            if height[index] > localMax:
                localMax = height[index]
            else:
                waterTrapped += ( localMax - height[index])
        
        # calculate trapping water between index len(maxCol) - 1 and last column
        localMax = 0
        for index in range( len(height) - 1, maxCol[len(maxCol) - 1], -1):
            if height[index] > localMax:
                localMax = height[index]
            else:
                waterTrapped += (localMax - height[index])
    
        # calculate trapping water among highest columns
        for index in range ( len(maxCol) - 1):
            pos = maxCol[index] + 1
            while pos < maxCol[index + 1]:
                waterTrapped += (maxHeight - height[pos])
                pos += 1
        
        return waterTrapped
        
        
        