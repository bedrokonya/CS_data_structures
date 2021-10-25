import typing as tp


class Node():
    def __init__(self, idx: int, left_child_idx: int = None, right_child: int = None):
        self.idx = idx
        self.left_child_idx = left_child_idx
        self.right_child_idx = right_child


class BinaryTree:
    def __init__(self, vertices_by_index: tp.List[tp.Tuple[str, int, int]], root_idx: int):
        self.root_idx = root_idx
        self.vertices = vertices_by_index

    def in_order_traversal(self):
        result: tp.List[str] = []
        self._in_order_traversal(self.root_idx, result)
        print(" ".join(result))

    def pre_order_traversal(self):
        result: tp.List[str] = []
        self._pre_order_traversal(self.root_idx, result)
        print(" ".join(result))

    def post_order_traversal(self):
        result: tp.List[str] = []
        self._post_order_traversal(self.root_idx, result)
        print(" ".join(result))

    def _in_order_traversal(self, node_idx: int, result: tp.List[str]) -> None:
        if node_idx == -1:
            return
        self._in_order_traversal(self.left_child_idx(node_idx), result)
        result.append(self.current_node_key(node_idx))
        self._in_order_traversal(self.right_child_idx(node_idx), result)

    def _pre_order_traversal(self, node_idx: int, result: tp.List[str]) -> None:
        if node_idx == -1:
            return
        result.append(self.current_node_key(node_idx))
        self._pre_order_traversal(self.left_child_idx(node_idx), result)
        self._pre_order_traversal(self.right_child_idx(node_idx), result)

    def _post_order_traversal(self, node_idx: int, result: tp.List[str]) -> None:
        if node_idx == -1:
            return
        self._post_order_traversal(self.left_child_idx(node_idx), result)
        self._post_order_traversal(self.right_child_idx(node_idx), result)
        result.append(self.current_node_key(node_idx))

    def left_child_idx(self, current_node_idx: int) -> int:
        return self.vertices[current_node_idx][1]

    def right_child_idx(self, current_node_idx: int) -> int:
        return self.vertices[current_node_idx][2]

    def current_node_key(self, current_node_idx: int) -> str:
        return self.vertices[current_node_idx][0]


def main():
    n = int(input())

    tree_descr: tp.List[tp.Tuple[str, int, int]] = []
    for i in range(n):
        key, left_idx, right_idx = input().strip().split(" ")
        tree_descr.append(tuple([key, int(left_idx), int(right_idx)]))

    tree = BinaryTree(tree_descr, 0)
    tree.in_order_traversal()
    tree.pre_order_traversal()
    tree.post_order_traversal()


if __name__ == "__main__":
    main()
