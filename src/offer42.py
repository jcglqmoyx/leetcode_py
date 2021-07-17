from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, res = 0, -10 ** 9
        for num in nums:
            sum = max(sum + num, num)
            res = max(res, sum)
        return res
