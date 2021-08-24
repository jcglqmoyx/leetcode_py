from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10 ** 8
        dist = [INF] * n
        dist[src] = 0
        for i in range(k + 1):
            cur = [0] * n
            for j in range(n):
                cur[j] = dist[j]
            for flight in flights:
                a, b, c = flight
                cur[b] = min(cur[b], dist[a] + c)
            for j in range(n):
                dist[j] = cur[j]
        return dist[dst] if dist[dst] != INF else -1
