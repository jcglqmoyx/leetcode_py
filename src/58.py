class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                j = i - 1
                while j >= 0 and s[j] != ' ':
                    j -= 1
                return i - j
        return length
