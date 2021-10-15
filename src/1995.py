from typing import List


# class Solution:
#     def countQuadruplets(self, nums: List[int]) -> int:
#         cnt, n = 0, len(nums)
#         for a in range(0, n - 3):
#             for b in range(a + 1, n - 2):
#                 for c in range(b + 1, n - 1):
#                     for d in range(c + 1, n):
#                         if nums[a] + nums[b] + nums[c] == nums[d]:
#                             cnt += 1
#         return cnt

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt, n = 0, len(nums)
        d = [0] * 205
        for i in range(1, n - 2):
            for j in range(0, i):
                d[nums[j] + nums[i]] += 1
            for j in range(i + 2, n):
                if nums[j] >= nums[i + 1]:
                    cnt += d[nums[j] - nums[i + 1]]
        return cnt
