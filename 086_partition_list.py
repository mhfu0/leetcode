# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# S1: Two pointers
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        less = ListNode(0)
        greater = ListNode(0)
        less_head = less
        greater_head = greater
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        greater.next = None
        less.next = greater_head.next
        return less_head.next

# S2: Queues
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        Q1 = []
        Q2 = []
        curr = head
        while curr:
            if curr.val < x:
                Q1.append(curr)
            else:
                Q2.append(curr)
            curr = curr.next
        if Q1:
            head = Q1[0]
            while Q1:
                node = Q1.pop(0)
                if Q1:
                    node.next = Q1[0]
            node.next = Q2[0] if Q2 else None
        else:
            head = Q2[0]
        while Q2:
            node = Q2.pop(0)
            if Q2:
                node.next = Q2[0]
        node.next = None
        return head
