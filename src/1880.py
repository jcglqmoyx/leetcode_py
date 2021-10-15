class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = b = c = 0
        for ch in firstWord:
            a = (a * 10) + ord(ch) - ord('a')
        for ch in secondWord:
            b = (b * 10) + ord(ch) - ord('b')
        for ch in targetWord:
            c = (c * 10) + ord(ch) - ord('c')
        return a + b == c
