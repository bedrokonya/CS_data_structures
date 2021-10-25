
class RandomTree:
    def __init__(self, num_vertices):
        # self.num_vertices = num_vertices
        self.vertices = [[] for _ in range(num_vertices)]
        self.root = None

    def add_child(self, parent_index: int, child_index: int) -> None:
        if parent_index == -1:
            self.root = parent_index
        else:
            self.vertices[parent_index].append(child_index)
