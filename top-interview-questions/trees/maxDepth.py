class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        if leftDepth >= rightDepth:
            return 1 + leftDepth
        else:
            return 1 + rightDepth