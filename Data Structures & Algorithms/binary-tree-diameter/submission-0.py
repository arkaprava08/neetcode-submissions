# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res=0

        def inOrder(root):
            nonlocal res
            if not root:
                return 0

            l=inOrder(root.left)
            r=inOrder(root.right)

            if (l+r) > res:
                res=l+r

            return max(l, r)+1
        
        inOrderOut = inOrder(root)
        if (inOrderOut-1 > res):
            res=inOrderOut-1
        print(res)

        return res


        

