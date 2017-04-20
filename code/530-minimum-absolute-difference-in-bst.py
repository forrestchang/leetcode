# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.array = []

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        self.array.append(root.val)
        if root.right:
            self.inorder(root.right)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorder(root)
        min_diff = self.array[1] - self.array[0]
        for i in range(2, len(self.array) - 1):
            if self.array[i + 1] - self.array[i] < min_diff:
                min_diff = self.array[i + 1] - self.array[i]
        return min_diff

if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    # root.left.right.left = TreeNode(8)
    # root.left.right.right = TreeNode(9)
    root = TreeNode(1)
    root.right = TreeNode(5)
    root.right.left = TreeNode(3)
    print(Solution().getMinimumDifference(root))
    assert Solution().getMinimumDifference(root) == 2
