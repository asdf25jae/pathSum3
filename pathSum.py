# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None: return 0
        elif sum == root.val: return 1
        else:
            left_path = self.pathSum(root.left, sum-root.val) + self.pathSum(root.left, sum)
            right_path = self.pathSum(root.right, sum-root.val) + self.pathSum(root.right,sum)
            return max(left_path, right_path)
