class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        for index in range(len(digits)):
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                digits.reverse()
                return digits
        digits.append(1)
        digits.reverse()
        return digits