"""Binary Search Tree implementation with basic methods"""
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        s = "["
        s += "n/a" if self.val is None else str(self.val)
        s += ",L "
        s += "n/a" if self.left is None else str(self.left.val)
        s += ",R "
        s += "n/a" if self.right is None else str(self.right.val)
        return s + "]"


class BSTree:
    root: TreeNode

    def __init__(self, val):
        root = TreeNode(val)
        self.root = root

    def add(self, new_val):
        cur_node = self.root
        inserted = False

        while not inserted:
            go_left = False
            if new_val >= cur_node.val:
                new_node = cur_node.right
            else:
                go_left = True
                new_node = cur_node.left

            if new_node is None:
                inserted = True
                new_node = TreeNode(new_val)
                if go_left:
                    cur_node.left = new_node
                else:
                    cur_node.right = new_node
            else:
                cur_node = new_node

    @staticmethod
    def inorder(node: TreeNode):
        res_list = []

        def _inorder(node: TreeNode, res_list: List[int]):
            if node is not None:
                _inorder(node.left, res_list)
                res_list.append(node.val)
                _inorder(node.right, res_list)

        _inorder(node, res_list)
        return res_list

    @staticmethod
    def postorder(node: TreeNode):
        res_list = []

        def _postorder(node: TreeNode, res_list: List[int]):
            if node is not None:
                _postorder(node.left, res_list)
                _postorder(node.right, res_list)
                res_list.append(node.val)

        _postorder(node, res_list)
        return res_list

    @staticmethod
    def preorder(node: TreeNode):
        res_list = []

        def _preorder(node: TreeNode, res_list: List[int]):
            if node is not None:
                res_list.append(node.val)
                _preorder(node.left, res_list)
                _preorder(node.right, res_list)

        _preorder(node, res_list)

        return res_list

    @staticmethod
    def count(node: TreeNode):
        if node is not None:
            return 1 + BSTree.count(node.left) + BSTree.count(node.right)
        return 0

    @staticmethod
    def height(node: TreeNode):
        if node is not None:
            left_height = BSTree.height(node.left)
            right_height = BSTree.height(node.right)
            return 1 + max(left_height, right_height)
        return 0

    def delete(self, val: int) -> bool:
        cur_node = self.root
        prev_node = self.root
        found = False

        while not found:
            if cur_node.val == val:
                found = True
            else:
                prev_node = cur_node
                if val > cur_node.val:
                    cur_node = cur_node.right
                else:
                    cur_node = cur_node.left

            if cur_node is None:
                found = True

        if cur_node is None:
            return False

        if cur_node.left is None and cur_node.right is None:
            if cur_node.val > prev_node.val:
                prev_node.right = None
            else:
                prev_node.left = None
        elif cur_node.left is None and cur_node.right is not None:
            prev_node.right = cur_node.right
        elif cur_node.left is not None and cur_node.right is None:
            prev_node.left = cur_node.left
        else:
            min_node, min_parent = BSTree._find_min(cur_node.right, cur_node)
            if min_node.val >= min_parent.val:
                min_parent.right = min_node.right
            else:
                min_parent.left = min_node.left

            cur_node.val = min_node.val

        return True

    @staticmethod
    def _find_min(node: TreeNode, parent: TreeNode) -> (TreeNode, TreeNode):
        found = False

        while not found:
            if node.left is not None:
                parent = node
                node = node.left
            else:
                found = True

        return node, parent


tree = BSTree(80)
tree.add(70)
tree.add(75)
tree.add(65)
tree.add(75)
tree.add(35)
tree.add(100)
tree.add(90)
tree.add(120)
tree.add(120)
tree.add(150)
tree.add(74)

print(f'in-order -> {BSTree.inorder(tree.root)}')
# print(f'pre-order -> {BSTree.preorder(tree.root)}')
# print(f'post-order -> {BSTree.postorder(tree.root)}')
# print(f'num nodes -> {BSTree.count(tree.root)}')
# print(f'height -> {BSTree.height(tree.root)}')

tree.delete(80)
tree.delete(150)
tree.delete(70)
print(f'in-order -> {BSTree.inorder(tree.root)}')