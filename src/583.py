class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)
        return n + m - f[n][m] * 2
