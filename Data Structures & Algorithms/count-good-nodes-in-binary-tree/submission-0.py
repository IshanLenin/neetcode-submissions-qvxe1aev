class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Helper function to perform DFS traversal
        # It keeps track of the maximum value seen so far along the path
        def dfs(node, maxVal):
            if not node:
                return 0  # Base case: null node contributes 0 good nodes

            # A node is "good" if its value is greater than or equal to all values in the path from root
            res = 1 if node.val >= maxVal else 0

            # Update the max value seen so far on the path
            maxVal = max(maxVal, node.val)

            # Recur for left and right subtrees and add their results
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res  # Return total number of good nodes for this subtree

        # Start DFS from the root, where the max value seen so far is root.val
        return dfs(root, root.val)
