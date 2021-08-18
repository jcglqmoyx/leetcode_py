from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        res = [[]] * numRows
        res[0], res[1] = [[1], [1, 1]]
        for row in range(2, numRows):
            res[row] = [1] * (row + 1)
            for i in range(1, row):
                res[row][i] = res[row - 1][i - 1] + res[row - 1][i]
        return res
