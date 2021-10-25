import typing as tp
import random
from collections import deque
from string import ascii_letters


class Node:
    def __init__(self,
                 value: tp.Any,
                 parent: tp.Optional["Node"] = None,
                 is_left: tp.Optional[bool] = None,
                 left_child: tp.Optional["Node"] = None,
                 right_child: tp.Optional["Node"] = None):

        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
        self.is_left = is_left
        self.size = None
        self.count_size()

    def count_size(self):
        self.size = 1
        if self.left_child:
            self.size += self.left_child.size
        if self.right_child:
            self.size += self.right_child.size

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right_child is None and self.left_child is None:
            line = f'({self.value} {self.size})'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right_child is None:
            lines, n, p, x = self.left_child._display_aux()
            s = f'({self.value} {self.size})'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left_child is None:
            lines, n, p, x = self.right_child._display_aux()
            s = f'({self.value} {self.size})'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left_child._display_aux()
        right, m, q, y = self.right_child._display_aux()
        s = f'({self.value} {self.size})'
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class SplayTreeImplicitKeys:
    def __init__(self, root: Node = None):
        self.root = root
        self.update_root(root)

    def update_root(self, root: Node):
        self.root = root
        if self.root:
            self.root.parent = None
            self.root.is_left = None
            self.root.count_size()

    # def insert(self, inserted_value: tp.Any):
    #     node_to_insert_after = self._search_while_can(inserted_value)
    #
    #     if node_to_insert_after:
    #         if node_to_insert_after.value == inserted_value:
    #             return
    #         new_node: Node = Node(value=inserted_value, parent=node_to_insert_after)
    #         if inserted_value >= node_to_insert_after.value:
    #             node_to_insert_after.right_child = new_node
    #             new_node.is_left = False
    #         else:
    #             node_to_insert_after.left_child = new_node
    #             new_node.is_left = True
    #         # if self.root:
    #         #     print('before splay')
    #         #     self.root.display()
    #         node_to_insert_after.count_sum()
    #         self._splay(new_node)
    #     else:
    #         self.root = Node(inserted_value)

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
    def display_trees(A, aname, B, bname):
        if A and B:
            if A.root and B.root:
                print(f"{aname}")
                print(f"{A.root.display()}")
                print("--")
                print(f"{bname}")
                print(f"{B.root.display()}")
            elif A.root:
                print(f"{aname}")
                print(f"{A.root.display()}")
                print("--")
                print(f"{bname}={B.root}")
            elif B.root:
                print(f"{aname}={A.root}")
                print("--")
                print(f"{bname}")
                print(f"{B.root.display()}")
        elif A:
            if A.root:
                print(f"{aname}")
                print(f"{A.root.display()}")
                print("--")
                print(f"{bname}={B}")
            else:
                print(f"{aname}={A}")
                print("--")
                print(f"{bname}={B}")
        elif B:
            if B.root:
                print(f"{aname}={A}")
                print("--")
                print(f"{bname}")
                print(f"{B.root.display()}")
            else:
                print(f"{aname}={A}")
                print("--")
                print(f"{bname}={B}")
        else:
            print("Both none")
        print("--------------")

    # def remove(self, value: int):
    #     node: tp.Optional[Node] = self._search_while_can(value)
    #     if node and node.value == value:
    #         self._splay(node)
    #         self.update_root(node.left_child)
    #         tree_r = SplayTreeImplicitKeys(node.right_child)
    #         self.merge(tree_r)
    @staticmethod
    def rope(initial_tree: "SplayTreeImplicitKeys", i: int, j: int, k: int):
        # here they use 1+ indexing
        tree_lt_i, tree_gte_i = SplayTreeImplicitKeys.split(initial_tree, i - 1)

        # SplayTreeImplicitKeys.display_trees(tree_lt_i, "tree_lt_i", tree_gte_i, "tree_gte_i") #debug


        tree_i_j, tree_gt_j = SplayTreeImplicitKeys.split(tree_gte_i, j - i + 1)

        # SplayTreeImplicitKeys.display_trees(tree_i_j, "tree_i_j", tree_gt_j, "tree_gt_j") #debug

        tree_to_merge_in: tp.Optional["SplayTreeImplicitKeys"] = SplayTreeImplicitKeys.merge(tree_lt_i, tree_gt_j)

        # SplayTreeImplicitKeys.display_trees(tree_to_merge_in, "tree_to_merge_in", None, "") #debug


        tree_lte_k, tree_gt_k = SplayTreeImplicitKeys.split(tree_to_merge_in, k)

        # SplayTreeImplicitKeys.display_trees(tree_lte_k, "tree_lte_k", tree_gt_k, "tree_gt_k") #debug

        tree_j = SplayTreeImplicitKeys.merge(tree_lte_k, tree_i_j)

        # SplayTreeImplicitKeys.display_trees(tree_j, "tree_j", None, "") #debug

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

        parent.count_size()
        node.count_size()
        if grandparent:
            grandparent.count_size()
        # if self.root:
        #     print(f'small rotation: node={node.value}')
        #     self.root.display()

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
                # if result and result[-1] >= top_node.value:
                #     return False
                result.append(top_node.value)
                current_node = top_node.right_child
                if current_node:
                    assert not current_node.is_left
        # return True
        return "".join(result)


def main():
    S: str = input()
    tree: SplayTreeImplicitKeys = SplayTreeImplicitKeys()
    for letter in S:
        new_tree = SplayTreeImplicitKeys(Node(letter))
        SplayTreeImplicitKeys.merge(tree, new_tree)

    q: int = int(input())

    for _ in range(q):
        i, j, k = map(int, input().split(" "))
        tree = SplayTreeImplicitKeys.rope(tree, i+1, j+1, k)
    print(tree.in_order_traversal())

    # tree = SplayTreeImplicitKeys(Node("a"))
    #
    # current_string: str = "a"
    # cmds = ['merge', 'rope', 'search']
    #
    # for _ in range(1000):
    #     cmd_idx = random.randint(0, len(cmds) - 1)
    #     rand_cmd = cmds[cmd_idx]
    #     if rand_cmd == 'merge':
    #         letter: str = random.choice(ascii_letters)
    #         print(f'merge letter {letter}')
    #         new_tree = SplayTreeImplicitKeys(Node(letter))
    #         tree = SplayTreeImplicitKeys.merge(tree, new_tree)
    #         current_string += letter
    #         tree_string = tree.in_order_traversal()
    #
    #         assert tree_string == current_string
    #
    #     if rand_cmd == 'rope':
    #         try:
    #             i: int = random.randint(0, len(current_string)-1)
    #             j: int = random.randint(i, len(current_string)-1)
    #             k: int = random.randint(0, len(current_string) - (j - i + 1))
    #             print(f'rope {i} {j} {k}')
    #             tree = SplayTreeImplicitKeys.rope(tree, i+1, j+1, k)
    #             substr_ij: str = current_string[i:j+1]
    #             left_str: str = current_string[0:i] + current_string[j+1:]
    #             if k == 0:
    #                 current_string = substr_ij + left_str
    #             else:
    #                 current_string = left_str[0:k] + substr_ij + left_str[k:]
    #             tree_string = tree.in_order_traversal()
    #             print(f'current_string={current_string}')
    #             print(f'tree_string={tree_string}')
    #             assert current_string == tree_string
    #         except KeyError:
    #             pass
    #
    #     if rand_cmd == 'search':
    #         rand_int = random.randint(0, len(current_string) - 1)
    #         print(f'finding value with idx={rand_int}')
    #         found_node = tree.search(rand_int + 1)
    #         assert current_string[rand_int] == found_node.value
    #
    #     if tree.root:
    #         print('tree after operation:')
    #         tree.root.display()
    #         print(f'true string: {current_string}')
    #         print('=======')
    #
    #     result_ = tree.in_order_traversal()
    #     assert len(result_) == len(current_string)

    # tree = SplayTreeImplicitKeys(Node("a"))
    # r = SplayTreeImplicitKeys(Node("r"))
    # u = SplayTreeImplicitKeys(Node("u"))
    # tree = SplayTreeImplicitKeys.merge(tree, r)
    # tree = SplayTreeImplicitKeys.merge(tree, u)
    # #aru rope 0 0 1
    # tree = SplayTreeImplicitKeys.rope(tree, 1, 1, 1)
    #
    # result_ = tree.in_order_traversal()
    # print(result_)
    # assert "rau" == result_


if __name__ == "__main__":
    main()