# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, result):
            if not root:
                result.append(None)
                return

            dfs(root.left, result)
            dfs(root.right, result)
            result.append(root.val)

        result1, result2 = [], []
        dfs(root, result1)
        dfs(subRoot, result2)
        
        for i in range(len(result1) - len(result2) + 1):
            if result1[i: i + len(result2)] == result2:
                return True

        return False


                

