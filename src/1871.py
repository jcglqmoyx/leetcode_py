class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        f, pre = [0] * (n + 1), [0] * (n + 1)
        f[1] = pre[1] = 1
        for i in range(2, n + 1):
            if s[i - 1] == '0' and i - minJump >= 1:
                if pre[i - minJump] > pre[max(1, i - maxJump) - 1]:
                    f[i] = 1
            pre[i] = pre[i - 1] + f[i]
        return True if f[n] else False
