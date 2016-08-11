# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(1+self.maxDepth(root.right),1+self.maxDepth(root.left)) 
 #       if root.left and root.right:
 #           return max(1+self.maxDepth(root.right),1+self.maxDepth(root.left))
 #           
 #       if root.right and not root.left:
 #           return 1+self.maxDepth(root.right)
 #       if root.left and not root.right:
 #          return 1+self.maxDepth(root.left)
        return 1