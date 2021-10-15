from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        t = ''
        for word in words:
            t += word
            if len(t) >= len(s):
                break
        return t == s
