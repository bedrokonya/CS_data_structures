import random
import typing as tp
from collections import deque
from string import ascii_letters

from custom_data_structures.splay_tree.node import Node
from custom_data_structures.splay_tree.splay_tree_implicit_keys import SplayTreeImplicitKeys

def main():
    # S: str = input()
    # tree: SplayTreeImplicitKeys = SplayTreeImplicitKeys()
    # for letter in S:
    #     new_tree = SplayTreeImplicitKeys(Node(letter))
    #     SplayTreeImplicitKeys.merge(tree, new_tree)
    #
    # q: int = int(input())
    #
    # for _ in range(q):
    #     i, j, k = map(int, input().split(" "))
    #     tree = SplayTreeImplicitKeys.rope(tree, i+1, j+1, k)
    # print(tree.in_order_traversal())

    tree = SplayTreeImplicitKeys(Node("a"))

    current_string: str = "a"
    cmds = ['merge', 'rope', 'search']

    for _ in range(1000):
        cmd_idx = random.randint(0, len(cmds) - 1)
        rand_cmd = cmds[cmd_idx]
        if rand_cmd == 'merge':
            letter: str = random.choice(ascii_letters)
            print(f'merge letter {letter}')
            new_tree = SplayTreeImplicitKeys(Node(letter))
            tree = SplayTreeImplicitKeys.merge(tree, new_tree)
            current_string += letter
            tree_string = tree.in_order_traversal()

            assert tree_string == current_string

        if rand_cmd == 'rope':
            try:
                i: int = random.randint(0, len(current_string)-1)
                j: int = random.randint(i, len(current_string)-1)
                k: int = random.randint(0, len(current_string) - (j - i + 1))
                print(f'rope {i} {j} {k}')
                tree = SplayTreeImplicitKeys.rope(tree, i+1, j+1, k)
                substr_ij: str = current_string[i:j+1]
                left_str: str = current_string[0:i] + current_string[j+1:]
                if k == 0:
                    current_string = substr_ij + left_str
                else:
                    current_string = left_str[0:k] + substr_ij + left_str[k:]
                tree_string = tree.in_order_traversal()
                print(f'current_string={current_string}')
                print(f'tree_string={tree_string}')
                assert current_string == tree_string
            except KeyError:
                pass

        if rand_cmd == 'search':
            rand_int = random.randint(0, len(current_string) - 1)
            print(f'finding value with idx={rand_int}')
            found_node = tree.search(rand_int + 1)
            assert current_string[rand_int] == found_node.value

        if tree.root:
            print('tree after operation:')
            tree.root.display()
            print(f'true string: {current_string}')
            print('=======')

        result_ = tree.in_order_traversal()
        assert len(result_) == len(current_string)

    tree = SplayTreeImplicitKeys(Node("a"))
    r = SplayTreeImplicitKeys(Node("r"))
    u = SplayTreeImplicitKeys(Node("u"))
    tree = SplayTreeImplicitKeys.merge(tree, r)
    tree = SplayTreeImplicitKeys.merge(tree, u)
    tree = SplayTreeImplicitKeys.rope(tree, 1, 1, 1)

    result_ = tree.in_order_traversal()
    print(result_)
    assert "rau" == result_


if __name__ == "__main__":
    main()