# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        node_stack = []
        state_stack = []
        node_stack.append(root)
        state_stack.append('L')
        
        num_list = []
        while node_stack:
            top = node_stack[-1]
            if state_stack[-1] == 'L':
                state_stack[-1] = 'R'
                if top.left:
                    node_stack.append(top.left)
                    state_stack.append('L')
            elif state_stack[-1] == 'R':
                state_stack[-1] = 'F'
                if top.right:
                    node_stack.append(top.right)
                    state_stack.append('L')
            else:
                state_stack.pop(-1)
                num_list.append(node_stack.pop(-1).val)
        return num_list

        
