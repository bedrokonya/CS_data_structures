from collections import deque

import typing as tp
from custom_data_structures.splay_tree.node import Node
from custom_data_structures.splay_tree.splay_tree_rotations import SplayTreeRotations


class SplayTree(SplayTreeRotations):
    def __init__(self, root=None):
        super().__init__(root)

    def insert(self, inserted_value: tp.Any):
        node_to_insert_after = self._search_while_can(inserted_value)

        if node_to_insert_after:
            if node_to_insert_after.value == inserted_value:
                return
            new_node: Node = Node(value=inserted_value, parent=node_to_insert_after)
            if inserted_value >= node_to_insert_after.value:
                node_to_insert_after.right_child = new_node
                new_node.is_left = False
            else:
                node_to_insert_after.left_child = new_node
                new_node.is_left = True

            node_to_insert_after.count_sum()
            self._splay(new_node)
        else:
            self.root = Node(inserted_value)

    def search(self, value: tp.Any) -> tp.Optional[Node]:
        found_node: tp.Optional[Node] = self._search_while_can(value)
        self._splay(found_node)
        if found_node and found_node.value == value:
            return found_node
        else:
            return None

    def remove(self, value: int):
        node: tp.Optional[Node] = self._search_while_can(value)
        if node and node.value == value:
            self._splay(node)
            self.update_root(node.left_child)
            tree_r = SplayTree(node.right_child)
            self.merge(tree_r)

    def split(self, value: tp.Any) -> tp.Optional["SplayTreeImplicitKeys"]:
        found_node: tp.Optional[Node] = self._search_while_can(value)
        if found_node:
            self._splay(found_node)
            if found_node.value <= value:
                r_child = found_node.right_child
                found_node.right_child = None
                self.update_root(found_node)
                new_tree: "SplayTreeImplicitKeys" = SplayTree(r_child)
            else:
                l_child = found_node.left_child
                found_node.left_child = None
                self.update_root(l_child)
                new_tree: "SplayTreeImplicitKeys" = SplayTree(found_node)
            return new_tree
        return None

    def merge(self, tree_to_merge_in: "SplayTreeImplicitKeys") -> None:
        if tree_to_merge_in:
            root_to_merge_in: tp.Optional[Node] = tree_to_merge_in.root
            node_with_max: tp.Optional[Node] = self._find_node_with_max()

            if node_with_max:
                self._splay(node_with_max)
                node_with_max.right_child = root_to_merge_in
                if node_with_max.right_child:
                    node_with_max.right_child.is_left = False
                    node_with_max.right_child.parent = node_with_max
                node_with_max.count_sum()
            else:
                self.update_root(root_to_merge_in)

    def sum(self, l: int, r: int) -> int:
        result = 0
        tree_gte_l: tp.Optional["SplayTreeImplicitKeys"] = self.split(l - 1)
        if tree_gte_l:
            tree_lt_r: tp.Optional["SplayTreeImplicitKeys"] = tree_gte_l.split(r)
            if tree_gte_l.root:
                result = tree_gte_l.root.sum
            else:
                result = 0
            tree_gte_l.merge(tree_lt_r)
        self.merge(tree_gte_l)
        return result

    def _search_while_can(self, value: tp.Any):
        prev_node: tp.Optional[Node] = None
        current_node: tp.Optional[Node] = self.root
        while current_node:
            if value == current_node.value:
                return current_node

            if value > current_node.value:
                prev_node, current_node = current_node, current_node.right_child
            else:
                prev_node, current_node = current_node, current_node.left_child
        return prev_node

    def _find_node_with_max(self) -> tp.Optional[Node]:
        current_node: tp.Optional[Node] = self.root
        while current_node and current_node.right_child:
            current_node = current_node.right_child
        return current_node

    def in_order_traversal(self, result: tp.List[int]) -> bool:
        if self.root is None:
            return True
        stack: deque = deque()
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
                if result and result[-1] >= top_node.value:
                    return False
                result.append(top_node.value)
                current_node = top_node.right_child
                if current_node:
                    assert not current_node.is_left
        return True
