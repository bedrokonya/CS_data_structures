import typing as tp
from collections import deque


class Node():
    def __init__(self, idx: int, left_child_idx: int = None, right_child: int = None):
        self.idx = idx
        self.left_child_idx = left_child_idx
        self.right_child_idx = right_child


class BinaryTree:
    def __init__(self, vertices_by_index: tp.List[tp.Tuple[int, int, int]], root_idx: int):
        self.root_idx = root_idx
        self.vertices = vertices_by_index

    def in_order_traversal(self):
        result: tp.List[int] = []
        stack: deque = deque()
        stack.append(self.root_idx)
        cur_vertex_idx = self.left_child_idx(self.root_idx)
        while len(stack) != 0 or cur_vertex_idx != -1:
            if cur_vertex_idx != -1:
                stack.append(cur_vertex_idx)
                cur_vertex_idx = self.left_child_idx(cur_vertex_idx)
            else:
                top_vertex_idx: int = stack.pop()
                if result and result[-1] >= self.current_node_key(top_vertex_idx):
                    print("INCORRECT")
                    return
                result.append(self.current_node_key(top_vertex_idx))
                cur_vertex_idx = self.right_child_idx(top_vertex_idx)
        print("CORRECT")

    def left_child_idx(self, current_node_idx: int) -> int:
        return self.vertices[current_node_idx][1]

    def right_child_idx(self, current_node_idx: int) -> int:
        return self.vertices[current_node_idx][2]

    def current_node_key(self, current_node_idx: int) -> int:
        return self.vertices[current_node_idx][0]


def main():
    n = int(input())

    tree_descr: tp.List[tp.Tuple[int, int, int]] = []
    for i in range(n):
        key, left_idx, right_idx = input().strip().split(" ")
        tree_descr.append(tuple([int(key), int(left_idx), int(right_idx)]))

    if tree_descr:
        tree = BinaryTree(tree_descr, 0)
        tree.in_order_traversal()
    else:
        print("CORRECT")

if __name__ == "__main__":
    main()

