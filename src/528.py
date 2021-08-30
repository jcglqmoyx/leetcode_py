import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.s = [w[0]]
        for i in range(1, len(w)):
            self.s.append(self.s[-1] + w[i])

    def pickIndex(self) -> int:
        p = random.randint(0, self.s[-1] - 1)
        l, r = 0, len(self.s) - 1
        while l < r:
            mid = (l + r) // 2
            if self.s[mid] > p:
                r = mid
            else:
                l = mid + 1
        return l
