class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            res += d[s[i]]
            for j in range(i - 1, -1, -1):
                if d[s[j]] < d[s[i]]:
                    res -= d[s[j]] * 2
                else:
                    break
        return res
