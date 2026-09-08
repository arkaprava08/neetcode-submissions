# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        depth=0

        def maxDepthHelper(root, depth):
            if not root:
                return 0
            
            leftDepth=maxDepthHelper(root.left, depth)
            rightDepth=maxDepthHelper(root.right, depth)
            depth=max(leftDepth, rightDepth)+1
            return depth


        return maxDepthHelper(root, 0)