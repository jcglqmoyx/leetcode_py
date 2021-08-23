class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        arr = [0] * (n + 1)
        arr[1] = 1
        res = 1
        for i in range(n + 1):
            if i % 2 == 0:
                arr[i] = arr[i // 2]
            else:
                arr[i] = arr[i // 2] + arr[(i + 1) // 2]
            res = max(res, arr[i])
        return res
