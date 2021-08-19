from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node: TreeNode, res: List[int]) -> None:
        if not node:
            return
        res.append(node.val)
        self.dfs(node.left, res)
        self.dfs(node.right, res)
