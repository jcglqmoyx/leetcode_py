class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 10 ** 9

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        self.dfs(root, 0)
        return self.res

    def dfs(self, node: TreeNode, depth: int) -> None:
        if not node:
            return
        if not node.left and not node.right:
            self.res = min(self.res, depth + 1)
            return
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
