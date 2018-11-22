# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, t1, t2):
        if not t1: return t2
        if not t2: return t1
        t1.left = self.helper(t1.left, t2.left)
        t1.right = self.helper(t1.right, t2.right)
        t1.val += t2.val
        return t1
        
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1: return t2
        if not t2: return t1
        t1 = self.helper(t1, t2)
        return t1
