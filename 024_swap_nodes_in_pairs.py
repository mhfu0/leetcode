# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#

# S1: recursive approach
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        second = head.next
        third = second.next
        second.next = head
        head.next = self.swapPairs(third)
        return second

# S2: iterative approach with much work-arounds
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p1 = head
        p2 = p1.next
        new_head = p2
        while p2 and p2.next:
            tmp = p2.next
            if p2.next.next:
                p1.next = p2.next.next
            else:  # handle list end (odd number of nodes)
                p1.next = p2.next
            p2.next = p1
            p1 = tmp
            p2 = p1.next
        if p2:  # handle list end (even number of nodes)
            p2.next = p1
            p1.next = None
        return new_head
