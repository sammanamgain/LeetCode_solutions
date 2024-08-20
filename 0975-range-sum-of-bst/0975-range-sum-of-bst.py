# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        # this is a problem of tree traversal

        # using inorder traversal

        self.sumvalue=0
        def traversal(node):
            if node==None:
                return 
            traversal(node.left)
            if node.val >=low and node.val<=high:
        
                self.sumvalue+=int(node.val)
            traversal(node.right)
            
        traversal(root)
        return self.sumvalue
        