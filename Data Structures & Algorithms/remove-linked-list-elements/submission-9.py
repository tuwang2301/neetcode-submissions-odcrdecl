# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        def remove(prev, node, val):
            if not node:
                return

            if node.val == val:
                prev.next = node.next
                remove(prev, node.next, val)
            else:
                remove(node, node.next, val)

        remove(dummy, dummy.next, val)
        return dummy.next
            