import typing as tp


class DisjointSet:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, i: int) -> int:
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, i: int, j: int) -> None:
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

def main():

    n, e, d = map(int, input().strip().split(" "))
    if n == 0:
        return

    d_set: DisjointSet = DisjointSet(n)

    for _ in range(e):
        x_i, x_j = map(int, input().strip().split(" "))
        d_set.union(x_i - 1, x_j - 1)
    for _ in range(d):
        x_i, x_j = map(int, input().strip().split(" "))
        if d_set.find(x_i - 1) == d_set.find(x_j - 1):
            print(0)
            return
    print(1)


if __name__ == "__main__":
    main()