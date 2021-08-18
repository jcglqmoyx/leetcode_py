class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        f = [[[0, 0, 0], [0, 0, 0]] for _ in range(n + 1)]
        f[0][0][0] = 1
        for i in range(n):
            for j in range(2):
                for k in range(3):
                    cur = f[i][j][k]
                    if not j:
                        f[i + 1][j + 1][0] = (f[i + 1][j + 1][0] + cur) % mod
                    if k + 1 <= 2:
                        f[i + 1][j][k + 1] = (f[i + 1][j][k + 1] + cur) % mod
                    f[i + 1][j][0] = (f[i + 1][j][0] + cur) % mod
        res = 0
        for j in range(2):
            for k in range(3):
                res = (res + f[n][j][k]) % mod
        return res
