from typing import List


def c(a: int, b: int) -> int:
    if a - b < b:
        return c(a, a - b)
    res = 1
    for i in range(b):
        res *= (a - i)
        res //= (i + 1)
    return res


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            res[i] = c(rowIndex, i)
        return res
