class TreeNode:
    def __init__(self, x: int):
        self.val: int = x
        self.left: 'TreeNode | None' = None
        self.right: 'TreeNode | None' = None


class Solution:
    def diameterOfBinaryTree(self, root: 'TreeNode | None') -> int:
        if root is None:
            return 0

        rootDiameter = self.getHeight(root.left) + self.getHeight(root.right)
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)

        return max(rootDiameter, max(leftDiameter, rightDiameter))

    def getHeight(self, root: 'TreeNode | None') -> int:
        if root is None:
            return 0
        left_height = self.getHeight(root.left) if root.left else 0
        right_height = self.getHeight(root.right) if root.right else 0
        return max(left_height, right_height) + 1


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

