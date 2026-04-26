# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Base Case
        if not root:
            return 0
        def dfs(node, max_val) -> int:
            # Base Case
            if not node:
                return 0
            # Perform the recursions for noth the left and right sub-nodes
            left = dfs(node.left, max(max_val, node.val))
            right = dfs(node.right, max(max_val, node.val))
            return left + right + (1 if node.val >= max_val else 0)
        return dfs(root, root.val)
