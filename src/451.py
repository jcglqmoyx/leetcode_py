import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = collections.Counter(s)
        a = sorted(cnt.items(), reverse=True, key=lambda x: x[1])
        res = ""
        for c, freq in a:
            res += c * freq
        return res
