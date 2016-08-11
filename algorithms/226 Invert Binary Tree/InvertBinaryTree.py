# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.left:
            tmp1=self.invertTree(root.left)
        else:
            tmp1=None
        if root.right:
            tmp2=self.invertTree(root.right)
        else:
            tmp2=None
        root.left=tmp2
        root.right=tmp1
        return root
        