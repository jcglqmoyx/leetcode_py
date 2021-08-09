class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l, r = self.maxDepth(root.left), self.maxDepth(root.right)
        return max(l, r) + 1
