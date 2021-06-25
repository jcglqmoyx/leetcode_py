from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = '0000'
        if target == start:
            return 0
        dead = set(deadends)
        if start in dead or target in dead:
            return -1
        dist = {start: 0}
        q = deque([])
        q.append(start)
        while len(q):
            t = q.popleft()
            for i in range(len(t)):
                for j in range(-1, 2, 2):
                    ch = t[i]
                    tmp = chr((ord(ch) - ord('0') + j + 10) % 10 + ord('0'))
                    s = t[:i] + tmp + t[i + 1:]
                    if s not in dead and s not in dist:
                        dist[s] = dist[t] + 1
                        if s == target:
                            return dist[s]
                        q.append(s)
        return -1
