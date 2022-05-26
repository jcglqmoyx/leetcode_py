from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        d = [0] * (n + 1)
        for i in range(n):
            d[(i + 1) % n] += 1
            d[(i + 1 + n - nums[i]) % n] -= 1
            if nums[i] <= i:
                d[0] += 1
        res = score = max_score = 0
        for i in range(n):
            score += d[i]
            if score > max_score:
                max_score = score
                res = i
        return res
