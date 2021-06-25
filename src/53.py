from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, s = nums[0], 0
        for num in nums:
            s = max(s + num, num)
            res = max(res, s)
        return res
