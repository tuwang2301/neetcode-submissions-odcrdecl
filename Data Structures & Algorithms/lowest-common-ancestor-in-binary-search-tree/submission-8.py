# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def ancestor(root, d, ancestors):
            if not root:
                return

            ancestors.append(root)

            if root.val == d.val:
                return

            if root.val < d.val:
                ancestor(root.right, d, ancestors)

            if root.val > d.val:
                ancestor(root.left, d, ancestors)

            return

        ancestor1, ancestor2 = [], []
        ancestor(root, p, ancestor1)
        ancestor(root, q, ancestor2)

        l = min(len(ancestor1), len(ancestor2))
        res = None
        for i in range(l):
            if ancestor1[i].val != ancestor2[i].val:
                break
            res = ancestor1[i]
        
        return res
