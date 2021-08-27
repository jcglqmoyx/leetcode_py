class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * numRows
        t, row = 1, 0
        for ch in s:
            if row == 0:
                t = 1
            elif row == numRows - 1:
                t = -1
            rows[row] += ch
            row += t
        return ''.join(rows)
