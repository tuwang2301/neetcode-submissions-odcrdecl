# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        start = head
        tail = None

        while start:
            print(start.val, tail.val if tail else None)
            if tail:
                tail.next = start

            curr = start
            prev = None

            while curr.next:
                prev = curr
                curr = curr.next
            
            tail = curr
            print(prev.val if prev else None, tail.val)
            if not prev:
                return
            prev.next = None

            next_start = start.next
            start.next = tail

            start = next_start

        