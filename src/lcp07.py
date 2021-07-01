from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        f = [0] * n
        f[0] = 1
        for i in range(k):
            tmp = [0] * n
            for r in relation:
                src, dst = r[0], r[1]
                tmp[dst] += f[src]
            f = tmp
        return f[n - 1]
