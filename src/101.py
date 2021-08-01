class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p and q:
            return False
        if not q and p:
            return False
        if p.val != q.val:
            return False
        return self.helper(p.left, q.right) and self.helper(p.right, q.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
