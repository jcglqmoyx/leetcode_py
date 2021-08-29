from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n, res = len(arr), 0
        for i in range(len(arr)):
            left_odd, right_odd, left_even, right_even = (i + 1) // 2, (n - i) // 2, (i + 2) // 2, (n - i + 1) // 2
            res += arr[i] * (left_odd * right_odd + left_even * right_even)
        return res
