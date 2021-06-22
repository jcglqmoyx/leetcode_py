from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    q.append([i, j])
        if not q or len(q) == n * m:
            return -1
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        res = 0
        while q:
            flag = False
            for k in range(len(q), 0, -1):
                t = q[0]
                q.pop(0)
                for i in range(0, 4):
                    x, y = t[0] + dx[i], t[1] + dy[i]
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == 0:
                        flag = True
                        q.append([x, y])
                        grid[x][y] = 1
            if flag:
                res += 1
        return res
