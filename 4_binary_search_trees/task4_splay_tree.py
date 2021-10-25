import typing as tp
import random
from collections import deque


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
        self.sum = self.value

    def count_sum(self):
        self.sum = self.value
        if self.left_child:
            self.sum += self.left_child.sum
        if self.right_child:
            self.sum += self.right_child.sum

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right_child is None and self.left_child is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right_child is None:
            lines, n, p, x = self.left_child._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left_child is None:
            lines, n, p, x = self.right_child._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left_child._display_aux()
        right, m, q, y = self.right_child._display_aux()
        s = '%s' % self.value
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


class SplayTree:
    def __init__(self, root=None):
        self.root = root
        self.update_root(root)

    def update_root(self, root):
        self.root = root
        if self.root:
            self.root.parent = None
            self.root.is_left = None
            self.root.count_sum()

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
            # if self.root:
            #     print('before splay')
            #     self.root.display()
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
                self.update_root(found_node) #// ???
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
                # print(f'sum tree:')
                # tree_gte_l.root.display()
                result = tree_gte_l.root.sum
            else:
                result = 0
            tree_gte_l.merge(tree_lt_r)
        self.merge(tree_gte_l)
        return result

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

        parent.count_sum()
        node.count_sum()
        if grandparent:
            grandparent.count_sum()
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
        # result: tp.List[int] = []
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





def main():
    # n: int = int(input())
    # s: int = 0
    # def f(i: int) -> int:
    #     return (i + s) % 1000000001
    #
    # tree = SplayTreeImplicitKeys()
    # for _ in range(n):
    #     line = input()
    #     if line.startswith("s"):
    #         _, l, r = line.strip().split(" ")
    #         l, r = int(l), int(r)
    #         s = tree.sum(f(l), f(r))
    #         print(s)
    #     else:
    #         op, i = line.strip().split(" ")
    #         i = int(i)
    #         if op == "+":
    #             tree.insert(f(i))
    #         if op == "-":
    #             tree.remove(f(i))
    #         if op == "?":
    #             node = tree.search(f(i))
    #             if node:
    #                 print("Found")
    #             else:
    #                 print("Not found")

    tree = SplayTree()
    set_ = set()
    cmds = ['insert', 'delete', 'find', 'sum']
    for _ in range(500):
        cmd_idx = random.randint(0, 3)
        rand_cmd = cmds[cmd_idx]
        rand_int = random.randint(0, 100)
        if rand_cmd == 'insert':
            print(f'inserting {rand_int}')
            set_.add(rand_int)
            tree.insert(rand_int)
        if rand_cmd == 'delete':
            print(f'deleting {rand_int}')
            tree.remove(rand_int)
            try:
                set_.remove(rand_int)
            except KeyError:
                pass
        if rand_cmd == 'find':
            print(f'finding {rand_int}')
            found_node = tree.search(rand_int)
            is_in_set = rand_int in set_
            assert (found_node is not None) is is_in_set
        if rand_cmd == 'sum':
            l = random.randint(0, 50)
            r = random.randint(50, 100)
            print(f'sum l={l} r={r}')
            print(tree.sum(l, r))
        if tree.root:
            print('after operation:')
            tree.root.display()
        result = []
        assert tree.in_order_traversal(result)
        # print(set_), print(result)
        assert len(result) == len(set_)


if __name__ == "__main__":
    main()