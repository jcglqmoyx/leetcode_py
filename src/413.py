from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        i = 0
        cnt = 0
        while i < len(nums) - 2:
            if nums[i + 1] * 2 == nums[i] + nums[i + 2]:
                j = i + 1
                while j < len(nums) - 2 and nums[j + 1] * 2 == nums[j] + nums[j + 2]:
                    j += 1
                length = j - i + 2
                cnt += (length - 2) * (length - 1) // 2
                i = j
            i += 1
        return cnt
