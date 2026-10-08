# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def diam(newRoot):
            nonlocal res
            if(newRoot == None):
                return 0
            res = max(res, diam(newRoot.left) + diam(newRoot.right))
            return 1 + max(diam(newRoot.left), diam(newRoot.right))
        diam(root)
        return res
        
        