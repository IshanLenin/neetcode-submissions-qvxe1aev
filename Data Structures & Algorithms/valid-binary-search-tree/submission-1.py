class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function that validates the BST
        # Each node must be within a valid (left, right) range
        def valid(node, left, right):
            if not node:
                return True  # An empty subtree is always valid

            # If the node value violates the BST property, return False
            if not (left < node.val < right):
                return False

            # Recursively validate the left and right subtrees
            # Left child must be in (left, node.val)
            # Right child must be in (node.val, right)
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        # Start the recursion with the full integer range
        return valid(root, float("-inf"), float("inf"))
