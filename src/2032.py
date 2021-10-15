from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = []
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        d = {}
        for x in s1:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        for x in s2:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        for x in s3:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        for x in d:
            if d[x] >= 2:
                res.append(x)
        return res
