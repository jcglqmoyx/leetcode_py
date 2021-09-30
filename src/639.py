class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(1, n + 1):
            for j in range(1, 27):
                a = s[i - 1]
                if j <= 9:
                    if a == '*' or ord(a) == j + ord('0'):
                        f[i] += f[i - 1]
                elif i >= 2:
                    b = s[i - 2]
                    y, x = j // 10, j % 10
                    if (a == '*' and x or ord(a) == x + ord('0')) and (b == '*' or ord(b) == y + ord('0')):
                        f[i] += f[i - 2]
                f[i] %= (10 ** 9 + 7)
        return f[n]
