from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        pre = [0] * (n + 2)
        for b in bookings:
            pre[b[0]] += b[2]
            pre[b[1] + 1] -= b[2]
        for i in range(1, len(pre)):
            pre[i] += pre[i - 1]
        for i in range(n):
            res[i] = pre[i + 1]
        return res
