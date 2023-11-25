# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# S1: Stack
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        Q1, Q2, QS = [], [], []
        while l1:
            Q1.append(l1.val)
            l1 = l1.next
        while l2:
            Q2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        while Q1 and Q2:
            d1, d2 = Q1.pop(-1), Q2.pop(-1)
            s = d1 + d2 + carry
            carry = s // 10
            QS.append(s % 10)
            
        if Q1 or Q2:
            QR = Q1 if Q1 else Q2
            while QR:
                s = QR.pop(-1) + carry
                carry = s // 10
                QS.append(s % 10)
                
        if carry > 0:
            QS.append(carry)
        
        head = curr = ListNode(0)
        while QS:
            curr.val = QS.pop(-1)
            if QS:
                curr.next = ListNode(0)
                curr = curr.next
        return head

# S2: Backtracking
# Alternative: left-padding
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(long, short, diff):
            if not long:
                return None, 0
            if diff > 0:
                res, carry = helper(long.next, short, diff - 1)
                val = long.val + carry
            else:
                res, carry = helper(long.next, short.next, diff)
                val = long.val + short.val + carry
            carry = val // 10
            node = ListNode()
            node.val = val % 10
            node.next = res
            return node, carry
        
        n1 = 0
        curr = l1
        while curr:
            n1 = n1 + 1
            curr = curr.next
        n2 = 0
        curr = l2
        while curr:
            n2 = n2 + 1
            curr = curr.next
        if n1 > n2:
            res, carry = helper(l1, l2, n1 - n2)
        else:
            res, carry = helper(l2, l1, n2 - n1)
        if carry > 0:
            dummy = ListNode(carry, res)
            res = dummy
        return res
