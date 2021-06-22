from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        s = list(s)
        s.sort()
        cur = []
        res = []
        used = [False] * len(s)

        def dfs(index: int) -> None:
            if index == len(s):
                res.append(''.join(cur))
                return
            for i in range(0, len(s)):
                if used[i] or i and s[i] == s[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                cur.append(s[i])
                dfs(index + 1)
                cur.pop()
                used[i] = False

        dfs(0)
        return res
