class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        rootDiameter = self.getHeight(root.left) + self.getHeight(root.right)
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)

        return max(rootDiameter, max(leftDiameter, rightDiameter))

    def getHeight(self, root : TreeNode) -> int:
        if root is None:
            return 0

        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1


four = TreeNode(4)
five = TreeNode(5)
two = TreeNode(2)
two.left = four
two.right = five
three = TreeNode(3)
one = TreeNode(1)
one.left = two
one.right = three

sol = Solution()
diameter = sol.diameterOfBinaryTree(one)

t = TreeNode(1)
t.left = TreeNode(2)
#diameter = sol.diameterOfBinaryTree(t)
print(f'{diameter}')

