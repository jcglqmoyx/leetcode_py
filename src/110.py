class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    flag = True

    def isBalanced(self, root: TreeNode) -> bool:
        self.dfs(root)
        return self.flag

    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        l, r = self.dfs(root.left), self.dfs(root.right)
        if abs(l - r) > 1:
            self.flag = False
            return 0
        return max(l, r) + 1
