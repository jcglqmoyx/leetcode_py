class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st, ts = {}, {}
        for i in range(len(s)):
            a, b = s[i], t[i]
            if a in st and st[a] != b or b in ts and ts[b] != a:
                return False
            st[a] = b
            ts[b] = a
        return True
