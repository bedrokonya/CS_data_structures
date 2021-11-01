import typing as tp
from collections import deque

from custom_data_structures.splay_tree.node import Node
from custom_data_structures.splay_tree.splay_tree_rotations import SplayTreeRotations


class SplayTreeImplicitKeys(SplayTreeRotations):
    def __init__(self, root=None):
        super().__init__(root)

    def get_left_child_size(self, node: Node) -> int:
        assert node
        return node.left_child.size if node.left_child else 0

    def search(self, idx: int) -> tp.Optional[Node]:
        if self.root is None or self.root.size < idx or idx < 1:
            return None
        current_node: tp.Optional[Node] = self.root
        while current_node:
            current_idx: int = self.get_left_child_size(current_node) + 1
            if current_idx == idx:
                return current_node
            if current_idx > idx:
                current_node = current_node.left_child
            if current_idx < idx:
                current_node = current_node.right_child
                idx = idx - current_idx

    @staticmethod
    def rope(initial_tree: "SplayTreeImplicitKeys", i: int, j: int, k: int):
        # here they use 1+ indexing
        tree_lt_i, tree_gte_i = SplayTreeImplicitKeys.split(initial_tree, i - 1)
        tree_i_j, tree_gt_j = SplayTreeImplicitKeys.split(tree_gte_i, j - i + 1)
        tree_to_merge_in: tp.Optional["SplayTreeImplicitKeys"] = SplayTreeImplicitKeys.merge(tree_lt_i, tree_gt_j)
        tree_lte_k, tree_gt_k = SplayTreeImplicitKeys.split(tree_to_merge_in, k)
        tree_j = SplayTreeImplicitKeys.merge(tree_lte_k, tree_i_j)

        return SplayTreeImplicitKeys.merge(tree_j, tree_gt_k)

    @staticmethod
    def split(tree_to_split: tp.Optional["SplayTreeImplicitKeys"], idx: int):
        new_tree = None
        if tree_to_split:
            found_node: tp.Optional[Node] = tree_to_split.search(idx)
            if found_node:
                tree_to_split._splay(found_node)
                r_child: tp.Optional[Node] = found_node.right_child
                if r_child:
                    found_node.right_child = None
                    tree_to_split.update_root(found_node)
                    new_tree: "SplayTreeImplicitKeys" = SplayTreeImplicitKeys(r_child)
        return (tree_to_split, new_tree) if idx != 0 else (new_tree, tree_to_split)

    @staticmethod
    def merge(tree_left: tp.Optional["SplayTreeImplicitKeys"], tree_right: tp.Optional["SplayTreeImplicitKeys"]) -> tp.Optional["SplayTreeImplicitKeys"]:
        if tree_left and tree_right:
            root_to_merge_in: tp.Optional[Node] = tree_right.root
            node_with_max_idx: tp.Optional[Node] = tree_left._find_the_rightest_node()
            if node_with_max_idx:
                tree_left._splay(node_with_max_idx)
                node_with_max_idx.right_child = root_to_merge_in
                if node_with_max_idx.right_child:
                    node_with_max_idx.right_child.is_left = False
                    node_with_max_idx.right_child.parent = node_with_max_idx
                node_with_max_idx.count_size()
                tree_right.update_root(node_with_max_idx)
            else:
                tree_left.update_root(root_to_merge_in)
        return tree_left if tree_left else tree_right

    def _find_the_rightest_node(self) -> tp.Optional[Node]:
        current_node: tp.Optional[Node] = self.root
        while current_node and current_node.right_child:
            current_node = current_node.right_child
        return current_node

    def in_order_traversal(self):
        if self.root is None:
            return True
        stack: deque = deque()
        result: tp.List[str] = []
        stack.append(self.root)
        current_node = self.root.left_child
        while len(stack) != 0 or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left_child
                if current_node:
                    assert current_node.is_left
            else:
                top_node: Node = stack.pop()

                result.append(top_node.value)
                current_node = top_node.right_child
                if current_node:
                    assert not current_node.is_left
        return "".join(result)