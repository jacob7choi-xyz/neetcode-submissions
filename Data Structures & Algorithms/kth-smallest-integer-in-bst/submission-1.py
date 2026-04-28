# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        self.k = k
        self.result = None
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return None
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
            dfs(node.right)
        dfs(root)
        return self.result