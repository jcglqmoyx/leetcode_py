from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if arr[mid] > arr[mid - 1]:
                l = mid
            else:
                r = mid - 1
        return l
