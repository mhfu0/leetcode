# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# [Note] Circular link can be created in the 1st pass

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        # Find the length of list
        count = 0
        curr = head
        while curr:
            count = count + 1
            curr = curr.next
        k = k % count
        if k == 0:
            return head

        # Find the starting node
        curr = head
        for _ in range(count, k+1, -1):
            curr = curr.next
        new_head = curr.next
        curr.next = None

        # Connect last node to head
        curr = new_head
        while curr.next:
            curr = curr.next
        curr.next = head
        return new_head
