# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res=True
        def validBST(root, lmin, rmax):
            if not root:
                return True
            
            if not (lmin < root.val < rmax):
                return False

            left = validBST(root.left, lmin, root.val)
            right = validBST(root.right, root.val, rmax)

            return left and right

        
        return validBST(root, float("-inf"), float("inf"))


        