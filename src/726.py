from typing import Dict


class Solution:
    u = 0

    def dfs(self, s: str) -> Dict[str, int]:
        res = {}
        while self.u < len(s):
            if s[self.u] == '(':
                self.u += 1
                t = self.dfs(s)
                self.u += 1
                cnt, k = 1, self.u
                while k < len(s) and s[k].isdigit():
                    k += 1
                if k > self.u:
                    cnt = int(s[self.u:k])
                self.u = k
                for atom, number in t.items():
                    if atom not in res:
                        res[atom] = 0
                    res[atom] += number * cnt
            elif s[self.u] == ')':
                break
            else:
                k, cnt = self.u + 1, 1
                while k < len(s) and s[k].islower():
                    k += 1
                atom = s[self.u:k]
                self.u = k
                while k < len(s) and s[k].isdigit():
                    k += 1
                if k > self.u:
                    cnt = int(s[self.u:k])
                self.u = k
                if atom not in res:
                    res[atom] = 0
                res[atom] += cnt
        return res

    def countOfAtoms(self, formula: str) -> str:
        res = ''
        t = self.dfs(formula)
        atoms = []
        for atom in t:
            atoms.append(atom)
        atoms.sort()
        for atom in atoms:
            res += atom
            if t[atom] > 1:
                res += str(t[atom])
        return res
