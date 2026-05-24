# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findK(self, root: Optional[TreeNode], k: int, arr: list):
        if root == None:
            return None
        
        self.findK(root.left, k, arr)

        arr.append(root.val)

        self.findK(root.right, k, arr)

        return root


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # print(" input - ", root.val)
        arr=[]
        self.findK(root, k, arr)

        print(arr)

        return arr[k-1]