# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    array = []

    def preorder(self, root):
        self.array.append(root.val)
        if root.left:
            self.preorder(root.left)
        if root.right:
            self.preorder(root.right)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.preorder(root)
        vals_set = list(set(self.array))
        if len(vals_set) == 0:
            return 0
        differences = []
        for i in range(len(vals_set)):
            for j in range(len(vals_set)):
                if i != j:
                    differences.append(abs(vals_set[i] - vals_set[j]))
        return min(differences)

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
    assert Solution().getMinimumDifference(root) == 2
