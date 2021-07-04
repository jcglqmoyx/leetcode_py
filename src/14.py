from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        min_length = 10000000
        for s in strs:
            min_length = min(min_length, len(s))
        if not min_length:
            return ''
        i = 0
        while True:
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return res
            res = strs[0][:i + 1]
            i += 1
            if i == min_length:
                break
        return res
