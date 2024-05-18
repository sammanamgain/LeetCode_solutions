# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.move=0
        def dfs(node):
            if not node:
                return [0,0]
            
            Leftcoin,Leftsize=dfs(node.left)
            Rightcoin,Rightsize=dfs(node.right)
            coin=node.val+Leftcoin+Rightcoin
            size=1+Leftsize+Rightsize
            self.move+=abs(coin-size)
            return [coin,size]

        dfs(root)
        return self.move


        