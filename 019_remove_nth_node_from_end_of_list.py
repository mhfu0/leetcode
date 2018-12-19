# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# One-pass solution
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: return head
        slow, fast = head, head
        
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


# Two-pass solution (AC)
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        n_from_head = length - n
        
        if n_from_head == 0:
            return head.next
        
        count = 0
        curr = head
        
        while curr and count != n_from_head - 1:
            curr = curr.next
            count += 1
        curr.next = curr.next.next
        return head
        
