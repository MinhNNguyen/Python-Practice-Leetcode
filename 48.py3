class Solution:

    # Swap 4 points at a time, from outer loop to inner loop

    def rotate(self, matrix: List[List[int]]) -> None:
        low, high = 0, len(matrix) - 1
        while low < high:
            for index in range(0, high - low):
                temp = matrix[high][high - index]
                matrix[high][high - index] = matrix[low + index][high]
                matrix[low + index][high] = matrix[low][low + index]
                matrix[low][low + index] = matrix[high - index][low] 
                matrix[high - index][low] = temp
            low += 1
            high -=1