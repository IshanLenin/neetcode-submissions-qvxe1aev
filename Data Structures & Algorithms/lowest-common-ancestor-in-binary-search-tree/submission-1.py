# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val: 
            #If both p and q are on greater than root, then update root to be root.right
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val: 
            #Otherwise, update root to be root.left
                cur = cur.left
            else: #Else, the lowest common ancestor has been found. 
                return cur