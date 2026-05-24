# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree2(self, preorder: List[int], inorder: List[int], limit) -> Optional[TreeNode]:
        if self.preIndx >= len(preorder):
            return None
        
        if inorder[self.inIndx] == limit:
            self.inIndx+=1
            return None
        
        root = TreeNode(preorder[self.preIndx])
        self.preIndx+=1
        root.left = self.buildTree2(preorder, inorder, root.val)
        root.right = self.buildTree2(preorder, inorder, limit)

        return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIndx=0
        self.inIndx=0
        return self.buildTree2(preorder, inorder, sys.maxsize)