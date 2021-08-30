from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i, n = 0, len(nums)
        while i < n:
            j = i + 1
            while j < n and nums[j] - nums[j - 1] == 1:
                j += 1
            size = j - i
            if size > 1:
                res.append(str(nums[i]) + '->' + str(nums[j - 1]))
            else:
                res.append(str(nums[i]))
            i = j
        return res
