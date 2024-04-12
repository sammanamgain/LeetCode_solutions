# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if val==root.val:
            return root
        elif val<root.val:
            return self.search(root.left,val)
        else:
            return self.search(root.right,val)
    def search(self,root: Optional[TreeNode],val:int) -> Optional[TreeNode]:
       
        if root==None:
            return None
        if val==root.val:
            return root
        elif val<root.val:
            return self.search(root.left,val)
        else:
            return self.search(root.right,val)


        