from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        f = [[1000000] * 3 for _ in range(n)]
        f[0][0] = f[0][2] = 1
        f[0][1] = 0
        for i in range(1, n):
            if obstacles[i] != 1:
                f[i][0] = f[i - 1][0]
            if obstacles[i] != 2:
                f[i][1] = f[i - 1][1]
            if obstacles[i] != 3:
                f[i][2] = f[i - 1][2]
            if obstacles[i] != 1:
                f[i][0] = min(f[i][0], min(f[i][1], f[i][2]) + 1)
            if obstacles[i] != 2:
                f[i][1] = min(f[i][1], min(f[i][0], f[i][2]) + 1)
            if obstacles[i] != 3:
                f[i][2] = min(f[i][2], min(f[i][0], f[i][1]) + 1)
        return min(f[n - 1][0], f[n - 1][1], f[n - 1][2])
