from collections import deque
from copy import deepcopy
from typing import List


class Solution:
    def get_status(self, board: List[List[int]]) -> str:
        res = ''
        for row in board:
            for x in row:
                res += str(x)
        return res

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        dist = {self.get_status(board): 0}
        target = [[1, 2, 3], [4, 5, 0]]
        if board == target:
            return 0
        q = deque([])
        q.append(board)
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        while q:
            t = q.popleft()
            x, y = 0, 0
            for i in range(0, 2):
                for j in range(0, 3):
                    if t[i][j] == 0:
                        x, y = i, j
            for i in range(0, 4):
                a, b = x + dx[i], y + dy[i]
                if a < 0 or a == 2 or b < 0 or b == 3:
                    continue
                r = deepcopy(t)
                r[a][b], r[x][y] = r[x][y], r[a][b]
                status = self.get_status(r)
                if status not in dist:
                    dist[status] = dist[self.get_status(t)] + 1
                    if r == target:
                        return dist[status]
                    q.append(r)
        return -1
