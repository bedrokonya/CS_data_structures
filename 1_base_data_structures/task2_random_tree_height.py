from queue import Queue

class RandomTree:
    def __init__(self, num_vertices):
        self.vertices = [[] for _ in range(num_vertices)]
        self.root = None

    def add_child(self, child_idx: int, parent_idx: int) -> None:
        if parent_idx == -1:
            self.root = child_idx
        else:
            self.vertices[parent_idx].append(child_idx)

    def get_height(self) -> int:

        if self.root is None:
            return 0

        height = 0
        q = Queue()
        q.put(self.root)

        while True:
            node_count = q.qsize()
            if node_count == 0:
                return height
            else:
                height += 1

            while node_count > 0:
                current_vertex = q.get()
                for child in self.vertices[current_vertex]:
                    q.put(child)
                node_count -= 1


def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    tree = RandomTree(n)
    tree_descr_str = input().strip()
    tree_descr_list  = list(map(int, tree_descr_str.split(" ")))
    for child_idx, parent_idx in enumerate(tree_descr_list):
        tree.add_child(child_idx, parent_idx)

    print(tree.get_height())



if __name__ == "__main__":
    main()