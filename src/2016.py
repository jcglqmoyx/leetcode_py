from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn = 10 ** 9 * 2
        res = -1
        for num in nums:
            res = max(res, num - mn)
            mn = min(mn, num)
        return res if res > 0 else -1
