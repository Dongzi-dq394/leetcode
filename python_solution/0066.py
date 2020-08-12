class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # New Solution: one pass (32ms: 83.82%)
        add = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i]+add!=10:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                add = 1
        return [1]+digits