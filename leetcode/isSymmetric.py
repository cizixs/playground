# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isSymmetric2(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        if node1 == None or node2 == None:
            return False

        if node1.val != node2.val:
            return False

        return self.isSymmetric2(node1.left, node2.right) and self.isSymmetric2(node1.right, node2.left)

    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True

        if root.left == None or root.right == None:
            return False

        return self.isSymmetric2(self.left, self.right)
