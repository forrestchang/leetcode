# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        sum = 0
        while queue:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
                if not current.left.left and not current.left.right:
                    sum += current.left.val
            if current.right:
                queue.append(current.right)
        return sum


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().sumOfLeftLeaves(root) == 24
