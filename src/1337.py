from typing import List


class Solution:
    def cnt(self, mat: List[List[int]], row: int):
        l, r = 0, len(mat[row]) - 1
        while l < r:
            mid = (l + r + 1) >> 1
            if mat[row][mid]:
                l = mid
            else:
                r = mid - 1
        return l + 1 if mat[row][l] else l

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        cnt = [0] * n
        for i in range(n):
            cnt[i] = self.cnt(mat, i)
        f = [x for x in range(n)]
        f.sort(key=lambda x: (cnt[x], x))
        res = f[:k]
        return res
