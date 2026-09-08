# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        out=[]

        def inOrderHelper(root):
            if not root:
                return
            
            inOrderHelper(root.left)
            out.append(root.val)
            inOrderHelper(root.right)
        
        inOrderHelper(root)
        return out
        