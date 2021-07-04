import collections
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = b = 0
        d = collections.Counter(nums)
        for i in range(1, len(nums) + 1):
            if d[i] == 2:
                a = i
            if d[i] == 0:
                b = i
        return [a, b]
