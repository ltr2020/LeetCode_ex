# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while len(stack):
            p, q = stack.pop()
            if p == None and q == None:
                continue # or continue dun't know why it's not right if it's retur True here
            elif p == None or q == None or p.val != q.val: 
                return False
            elif p.val == q.val: # else:
                stack.extend([(q.right,p.right),(q.left,p.left)])
        return True
        