# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def traverse(node, l1, l2):
            if not node:
                return
            
            l1.append(node.val)
            traverse(node.next, l1, l2)
            l2.append(node.val)

        l1, l2 = [], []
        traverse(head, l1, l2)

        return l1 == l2