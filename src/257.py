from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root.left and not root.right:
            return [str(root.val)]
        res = []

        def dfs(node: TreeNode, s: str) -> None:
            if not node:
                return
            s += "->" + str(node.val)
            if not node.left and not node.right:
                res.append(s)
            if node.left:
                dfs(node.left, s)
            if node.right:
                dfs(node.right, s)

        dfs(root.left, str(root.val))
        dfs(root.right, str(root.val))
        return res
