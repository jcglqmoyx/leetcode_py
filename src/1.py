from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(0, len(nums)):
            if m.__contains__(target - nums[i]):
                return [m[target - nums[i]], i]
            m[nums[i]] = i
        return []
