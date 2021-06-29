class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if not n:
            return 0
        ne = [-1] * n
        i, j = 1, -1
        while i < n:
            while j != -1 and needle[i] != needle[j + 1]:
                j = ne[j]
            if needle[i] == needle[j + 1]:
                j += 1
            ne[i] = j
            i += 1

        i, j = 0, -1
        while i < m:
            while j != -1 and haystack[i] != needle[j + 1]:
                j = ne[j]
            if haystack[i] == needle[j + 1]:
                j += 1
            if j == n - 1:
                return i - j
            i += 1
        return -1
