from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        while True:
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j < len(nums):
                i += 1
            else:
                break
            nums[i] = nums[j]
        return i + 1
