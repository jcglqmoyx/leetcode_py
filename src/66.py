from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, n = 0, len(digits)
        digits[-1] += 1
        for i in range(n - 1, -1, -1):
            sum = digits[i] + carry
            digits[i] = sum % 10
            if sum <= 9:
                return digits
            carry = sum // 10
        res = [0] * (n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            res[i] = digits[i - 1]
        return res
