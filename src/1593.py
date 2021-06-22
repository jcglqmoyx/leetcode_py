class Solution:
    def __init__(self):
        self.res = 0

    def maxUniqueSplit(self, s: str) -> int:
        string_set = set()

        def dfs(s: str, index: int) -> None:
            if index == len(s):
                self.res = max(self.res, len(string_set))
                return
            for size in range(1, len(s) - index + 1):
                sub = s[index: index + size]
                if sub in string_set:
                    continue
                string_set.add(sub)
                dfs(s, index + size)
                string_set.remove(sub)

        dfs(s, 0)
        return self.res
