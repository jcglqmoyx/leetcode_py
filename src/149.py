from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        for p in points:
            ss = vs = 0
            d = {}
            for q in points:
                if q == p:
                    ss += 1
                elif q[0] == p[0]:
                    vs += 1
                else:
                    slope = (p[1] - q[1]) / (p[0] - q[0])
                    d[slope] = d.get(slope, 0) + 1
            cnt = vs
            for k in d:
                cnt = max(cnt, d[k])
            res = max(res, cnt + ss)
        return res
