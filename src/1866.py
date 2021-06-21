class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        f = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                f[i][j] = f[i - 1][j - 1] + (i - 1) * f[i - 1][j]
        return f[n][k] % MOD
