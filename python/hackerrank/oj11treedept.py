# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root, n=0):
        if not root:
            return n

        if root.left is None and root.right is None:
            return n + 1

        return min(self.minDepth(root.left, n+1), self.minDepth(root.right, n+1)) +1



