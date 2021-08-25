from typing import List


class Solution:
    def dfs(self, graph: List[List[int]], start: int, paths: List[List[int]], path: List[int]) -> None:
        if start == len(graph) - 1:
            paths.append(path[:])
            return
        for ne in graph[start]:
            path.append(ne)
            self.dfs(graph, ne, paths, path)
            path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path, paths = [], []
        path.append(0)
        self.dfs(graph, 0, paths, path)
        return paths
