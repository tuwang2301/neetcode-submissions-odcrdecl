# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if ((q is None and p is not None) or (q is not None and p is None)):
            return False

        if ((q is not None and p is not None) and (q.val != p.val)):
            return False

        if (q is None and p is None):
            return True

        checkLeft = self.isSameTree(p.left, q.left)
        checkRight = self.isSameTree(p.right, q.right)
        return checkLeft and checkRight