# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findK(self, root: Optional[TreeNode], k: int):
        if root == None:
            return None
        
        self.findK(root.left, k)

        self._c+=1
        # print("ark - ", root.val, " <> ", self._c)

        if k == self._c:
            self._out = root.val

        self.findK(root.right, k)

        return root


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        print(" input - ", root.val)
        self._c=0
        self.findK(root, k)

        return self._out