# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Write Base Cases first
        if not subRoot:
            return True
        if not root and subRoot:
            return False
        def isSameTree(node: Optional[TreeNode], subNode: Optional[TreeNode]) -> bool:
            if not node and not subNode:
                return True
            if not node or not subNode:
                return False
            return node.val == subNode.val and isSameTree(node.left, subNode.left) and isSameTree(node.right, subNode.right)
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)