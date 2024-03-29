# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        return self.checkSymmetric(root.left,root.right)
    
    
    def checkSymmetric(self,left,right):
        if(left==None and right==None): 
            return True
        if(left==None or right==None or left.val!=right.val):
            return False
        return self.checkSymmetric(left.left,right.right) and self.checkSymmetric(left.right,right.left)