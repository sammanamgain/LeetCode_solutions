# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        stack=[]
        stack.append(root)
        def recursion():
            if(len(stack)==0):
                return 
            temp=[]          
            for i in range(len(stack)):
                node=stack.pop(0)
                if node==None:
                    continue
                temp.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            if len(temp)!=0:
                result.append(temp)
            recursion()
        recursion()
        return result


