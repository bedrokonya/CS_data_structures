import typing as tp

from custom_data_structures.splay_tree.node import Node


class SplayTreeRotations:
    def __init__(self, root: Node = None):
        self.root = root
        self.update_root(root)

    def update_root(self, root: Node):
        self.root = root
        if self.root:
            self.root.parent = None
            self.root.is_left = None
            self.root.update_metrics()

    def _small_rotation(self, node: Node):
        parent = node.parent
        grandparent: tp.Optional[Node] = parent.parent
        is_parent_left_child: tp.Optional[bool] = parent.is_left
        is_node_left: bool = node.is_left

        if grandparent:
            if is_parent_left_child:
                grandparent.left_child = node
            else:
                grandparent.right_child = node
        node.is_left = is_parent_left_child
        node.parent = grandparent

        if is_node_left: # zig
            node_right_child: tp.Optional[Node] = node.right_child
            node.right_child = parent
            parent.left_child = node_right_child
            if parent.left_child:
                parent.left_child.is_left = True
                parent.left_child.parent = parent
            parent.parent = node
            parent.is_left = False
        else: # zag
            node_left_child: tp.Optional[Node] = node.left_child
            node.left_child = parent
            parent.right_child = node_left_child
            if parent.right_child:
                parent.right_child.is_left = False
                parent.right_child.parent = parent
            parent.parent = node
            parent.is_left = True

        parent.update_metrics()
        node.update_metrics()
        if grandparent:
            grandparent.update_metrics()

    def _big_rotation(self, node: Node, parent: Node):
        if node.is_left != parent.is_left:
            #zigzag or zagzig
            self._small_rotation(node)
            self._small_rotation(node)
        else:
            #zigzig or zagzag
            self._small_rotation(parent)
            self._small_rotation(node)

    def _splay(self, node: Node) -> None:
        if self.root is node or node is None:
            return
        while node.parent:
            parent, grandparent = node.parent, node.parent.parent
            if parent and grandparent:
                self._big_rotation(node, parent)
            else:
                self._small_rotation(node)
        self.root = node
