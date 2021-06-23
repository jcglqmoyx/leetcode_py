from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        for num in nums:
            num = abs(num)
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        return n + 1
