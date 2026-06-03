# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, result):
            if not root:
                return
            
            dfs(root.left, result)
            result.append(root)
            dfs(root.right, result)

        res = []
        dfs(root, res)

        for i in range(1, len(res)):
            if res[i].val <= res[i-1].val:
                return False
            
        return True