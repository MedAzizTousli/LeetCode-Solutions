# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node, value):
        if not node:
            return None
        if node.val == value:
            return node
        elif node.val > value:
            return self.dfs(node.left, value)
        else:
            return self.dfs(node.right, value)

    def searchBST(self, root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        return self.dfs(root, value)