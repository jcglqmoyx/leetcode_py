import bisect
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        seq = []
        d = {}
        for i in range(len(target)):
            d[target[i]] = i
        for num in arr:
            if num not in d:
                continue
            idx = d[num]
            if not seq or seq[-1] < idx:
                seq.append(idx)
            else:
                pos = bisect.bisect_left(seq, idx)
                seq[pos] = idx
        return len(target) - len(seq)
