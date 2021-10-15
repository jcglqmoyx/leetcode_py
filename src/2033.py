from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        res = 0
        nums = []
        for row in grid:
            for num in row:
                nums.append(num)
        nums.sort()
        mid = nums[len(nums) // 2]
        for num in nums:
            if (num - mid) % x:
                return -1
            res += abs(num - mid) // x
        return res
