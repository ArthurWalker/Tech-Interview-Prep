class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closest = root.val  # track closest value

        def dfs(node):
            if not node:
                return

            # Update closest if current node is closer, or equally close but smaller
            if abs(node.val - target) < abs(self.closest - target) or \
               (abs(node.val - target) == abs(self.closest - target) and node.val < self.closest):
                self.closest = node.val

            # Recurse into the side that may contain closer values
            if target < node.val:
                dfs(node.left)
            elif target > node.val:
                dfs(node.right)
            # If target == node.val, no need to search further
            else:
                return

        dfs(root)
        return self.closest
