from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = k = 0
        while j < len(chars):
            chars[i] = chars[j]
            i += 1
            k = j
            while k < len(chars) and chars[k] == chars[j]:
                k += 1
            if k - j > 1:
                s = str(k - j)
                for c in s:
                    chars[i] = c
                    i += 1
            j = k
        return i
