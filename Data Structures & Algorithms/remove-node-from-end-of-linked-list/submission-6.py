# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0

        while curr:
            size += 1
            curr = curr.next

        count = 0
        prev = None
        curr = head

        while curr:
            print(count, curr.val)
            if count == size - n:
                if count == 0:
                    head = curr.next
                    return head
                tmp = curr.next
                prev.next = tmp
                curr.next = None
                curr = tmp
                return head
            
            prev = curr
            curr = curr.next
            count += 1

        return head

        