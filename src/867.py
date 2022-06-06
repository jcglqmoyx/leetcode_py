from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = matrix[j][i]
        return res
