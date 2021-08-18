class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    flag = False

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return self.flag
        self.dfs(root, root.val, targetSum)
        return self.flag

    def dfs(self, node: TreeNode, sum: int, target: int) -> None:
        if not node.left and not node.right and sum == target:
            self.flag = True
            return
        if node.left: self.dfs(node.left, sum + node.left.val, target)
        if node.right: self.dfs(node.right, sum + node.right.val, target)
