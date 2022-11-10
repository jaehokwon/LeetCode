# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            res = ''
            if node:
                res += str(node.val)
                if node.left or node.right:
                    res += '(' + dfs(node.left) + ')'
                if node.right:
                    res += '(' + dfs(node.right) + ')'
            return res
        return dfs(root)