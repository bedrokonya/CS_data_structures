import typing as tp
import sys

sys.setrecursionlimit(2 * 10**5)

class BinaryTree:
    def __init__(self, vertices_by_index: tp.List[tp.Tuple[int, int, int]], root_idx: int):
        self.root_idx = root_idx
        self.vertices = vertices_by_index

    def recursive_check(self, subtree_root_idx: int, min_val=float("-inf"), max_val=float("inf")):
        if subtree_root_idx == -1:
            return True
        current_key = self.key(subtree_root_idx)
        left_idx, right_idx = self.left_child_idx(subtree_root_idx), self.right_child_idx(subtree_root_idx)
        if current_key <= min_val or current_key >= max_val:
            return False
        left_check = self.recursive_check(left_idx, min_val, current_key)
        right_check = self.recursive_check(right_idx, current_key - 1, max_val)
        return left_check and right_check

    def left_child_idx(self, current_node_idx: int) -> int:
        return self.vertices[current_node_idx][1]

    def right_child_idx(self, current_node_idx: int) -> int:
        return self.vertices[current_node_idx][2]

    def key(self, current_node_idx: int) -> int:
        return self.vertices[current_node_idx][0]


def main():
    n = int(input())

    tree_descr: tp.List[tp.Tuple[int, int, int]] = []
    for i in range(n):
        tree_descr.append(tuple(map(int, input().strip().split(" "))))

    if tree_descr:
        tree = BinaryTree(tree_descr, 0)
        print("CORRECT") if tree.recursive_check(0) else print("INCORRECT")
    else:
        print("CORRECT")


if __name__ == "__main__":
    main()

