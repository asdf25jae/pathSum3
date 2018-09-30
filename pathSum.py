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
        else:
            return self.pathSumFrom(root, sum) +
        self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumFrom(self, root, sum):
        if root == None: return 0
        else:
            if root.val == sum: sum_0 = 1
            if root.val != sum: sum_0 = 0
            return sum_0 + self.pathSumFrom(root.left, sum-root.val) +
             self.pathSumFrom(root.right, sum-root.val)
