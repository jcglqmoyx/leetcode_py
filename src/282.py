from typing import List

expr = []


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)

        def dfs(u: int, cur: int, last: int) -> None:
            global expr
            if u == n:
                if cur == target:
                    res.append(''.join(expr))
                return
            val = 0
            size = len(expr)
            if u:
                expr += '0'
            for j in range(u, n):
                if not j == u and num[u] == '0':
                    break
                expr += num[j]
                val = val * 10 + ord(num[j]) - ord('0')
                if not u:
                    dfs(j + 1, val, val)
                else:
                    expr[size] = '+'
                    dfs(j + 1, cur + val, val)
                    expr[size] = '-'
                    dfs(j + 1, cur - val, -val)
                    expr[size] = '*'
                    dfs(j + 1, cur - last + val * last, val * last)
            expr = expr[:size]

        dfs(0, 0, 0)
        return res
