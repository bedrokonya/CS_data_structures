import typing as tp


class DisjointSet:
    def __init__(self, n: int, records_num: tp.List[int]):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.records_num = records_num
        self.current_max = max(self.records_num)
        assert n == len(records_num)

    def find(self, i: int) -> int:
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, i: int, j: int) -> None:
        # i dest, j source
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
            self.records_num[i_id] += self.records_num[j_id]
            if self.current_max < self.records_num[i_id]:
                self.current_max = self.records_num[i_id]
            self.records_num[j_id] = self.records_num[i_id]

        else:
            self.parent[i_id] = j_id
            self.records_num[j_id] += self.records_num[i_id]
            if self.current_max < self.records_num[j_id]:
                self.current_max = self.records_num[j_id]
            self.records_num[i_id] = self.records_num[j_id]
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

def main():

    n, m = map(int, input().strip().split(" "))
    if n == 0 or m == 0:
        return

    table_sizes: tp.List[int] = list(map(int, input().strip().split(" ")))

    d_set: DisjointSet = DisjointSet(n, table_sizes)
    for i in range(m):
        dest, source = map(int, input().strip().split(" "))
        d_set.union(dest - 1, source - 1)
        print(d_set.current_max)


if __name__ == "__main__":
    main()