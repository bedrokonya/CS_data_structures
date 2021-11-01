import random
from custom_data_structures.splay_tree.splay_tree import SplayTree


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
        assert len(result) == len(set_)


if __name__ == "__main__":
    main()
