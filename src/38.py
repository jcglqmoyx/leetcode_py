class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = '1'
        for i in range(2, n + 1):
            t = ''
            j = 0
            while j < len(s):
                k = j + 1
                while k < len(t) and s[k] == s[k - 1]:
                    k += 1
                cnt = k - j
                j = k - 1
                t += str(cnt) + s[j]
                j += 1
            s = t
        return s
