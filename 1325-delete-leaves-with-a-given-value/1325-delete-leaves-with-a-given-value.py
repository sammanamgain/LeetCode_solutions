# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # recurssion
        # lets reach to last left and right node
        if root==None:
            return None
        root.left=self.removeLeafNodes(root.left,target)
        root.right=self.removeLeafNodes(root.right,target)


        # for leaf nodes
        if not root.left and not root.right and root.val==target:
            return None

        return root