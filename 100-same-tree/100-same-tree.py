# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None: # base case: both empty -> same tree. Another way to write it "if not p and not q:"
            return True 
        if p == None or q == None: # base case: if one of them is empty --> not the same tree
            return False
        if p.val != q.val: # base case: both not empty but diff val -> diff tree
            return False
        
        return (self.isSameTree(p.left, q.left) and\
                self.isSameTree(p.right, q.right))