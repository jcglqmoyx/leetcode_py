from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def construct(self, nums: List[int], l: int, r: int) -> TreeNode:
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.construct(nums, l, mid - 1)
        root.right = self.construct(nums, mid + 1, r)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.construct(nums, 0, len(nums) - 1)
