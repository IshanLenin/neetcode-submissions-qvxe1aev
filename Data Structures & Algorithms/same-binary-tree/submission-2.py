# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #If there is no root node
            return True
        if p and q and p.val == q.val: #If node value is the same.
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) #Recursion on same direction node values.
        else:
            return False