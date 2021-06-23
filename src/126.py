from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        paths = []
        path = []
        dist = {beginWord: 0}
        q = [beginWord]
        s = set(wordList)

        def dfs(word: str):
            if word == beginWord:
                path.reverse()
                tmp = []
                for x in path:
                    tmp.append(x)
                paths.append(tmp)
                path.reverse()
            else:
                for idx in range(len(word)):
                    for c in range(ord('a'), ord('z') + 1):
                        p = word[:idx] + chr(c) + word[idx + 1:]
                        if p in dist and dist[p] + 1 == dist[t]:
                            path.append(p)
                            dfs(p)
                            path.pop()

        while q:
            t = q[0]
            q.pop(0)
            for i in range(len(t)):
                for ch in range(ord('a'), ord('z') + 1):
                    r = t[:i] + chr(ch) + t[i + 1:]
                    if r in s and r not in dist:
                        dist[r] = dist[t] + 1
                        if r == endWord:
                            break
                        q.append(r)
        if endWord not in dist:
            return paths
        path.append(endWord)
        dfs(endWord)
        return paths
