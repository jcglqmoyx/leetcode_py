from typing import List


def dist(s: List[int], t: List[int]) -> int:
    return abs(s[0] - t[0]) + abs(s[1] - t[1])


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        d = dist([0, 0], target)
        for ghost in ghosts:
            if dist(ghost, target) <= d:
                return False
        return True
