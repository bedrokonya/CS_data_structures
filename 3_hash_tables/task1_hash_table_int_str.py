# import math
import typing as tp

class HashTable:
    def __init__(self):
        self.x_powers = [97 ** i for i in range(7)]
        self.m = 10**5
        self.direct_adress_table = [None for _ in range(self.m)]

    def hash(self, key: str) -> int:
        hash_value = 0
        for i in range(len(key)):
            hash_value += self.x_powers[i] * ord(key[i])
        return hash_value % self.m

    def add(self, key_number: str, name: str):
        hash_value = self.hash(key_number)
        value: tp.Optional[tp.List[tp.Tuple[str, str]]] = self.direct_adress_table[hash_value]
        if value is None:
            self.direct_adress_table[hash_value] = [(key_number, name)]
        else:
            numbers = [t[0] for t in value]
            try:
                idx = numbers.index(key_number)
                value[idx] = (key_number, name)
            except ValueError:
                value.append((key_number, name))

    def find(self, key_number: str):
        value = self.direct_adress_table[self.hash(key_number)]
        if value:
            for tuple in value:
                if tuple[0] == key_number:
                    print(tuple[1])
                    return
            print("not found")
        else:
            print("not found")

    def delete(self, key_number):
        value = self.direct_adress_table[self.hash(key_number)]
        if value:
            numbers = [t[0] for t in value]
            try:
                idx = numbers.index(key_number)
                value.pop(idx)
            except ValueError:
                pass

    def __str__(self):
        result_str = ""
        for i, value in enumerate(self.direct_adress_table):
            if value:
                result_str += f"idx={i} {value} "

        return result_str

    # def get_ith_digit(self, number: int, i: int):
    #     return number // 10**i % 10
    #
    # def get_length_of_int(self, number: int):
    #     return int(math.log10(number)) + 1 if number > 0 else 1

def main():
    n = int(input().strip())
    table = HashTable()
    for _ in range(n):
        cmd = input().strip()
        if cmd.startswith("add"):
            number, name = cmd.split(" ")[1:3]
            table.add(number, name)
        if cmd.startswith("find"):
            number = cmd.split(" ")[1]
            table.find(number)
        if cmd.startswith("del"):
            number = cmd.split(" ")[1]
            table.delete(number)
        # print(table)


if __name__ == "__main__":
    main()