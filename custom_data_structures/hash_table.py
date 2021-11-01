import typing as tp
from collections import deque

class HashTable:
    def __init__(self, m: int):
        self.x = 263
        self.max_string_length = 15
        self.x_powers = [self.x ** i for i in range(self.max_string_length)]
        self.m = m
        self.p = 1000000007
        self.direct_adress_table = [None for _ in range(self.m)]

    def hash(self, key: str) -> int:
        hash_value = 0
        for i in range(len(key)):
            hash_value += (self.x_powers[i] * ord(key[i])) % self.p
        result = (hash_value % self.p) % self.m
        return result

    def add(self, key_str: str):
        hash_value: int = self.hash(key_str)
        strings_with_hash: tp.Optional[tp.Deque[str]] = self.direct_adress_table[hash_value]
        if strings_with_hash is None:
            self.direct_adress_table[hash_value] = deque([key_str])
        else:
            try:
                strings_with_hash.index(key_str)
            except ValueError:
                strings_with_hash.appendleft(key_str)

    def find(self, key_str: str):
        strings_with_hash: tp.Optional[tp.Deque[str]] = self.direct_adress_table[self.hash(key_str)]
        if strings_with_hash:
            for value in strings_with_hash:
                if value == key_str:
                    print("yes")
                    return
            print("no")
        else:
            print("no")

    def delete(self, key_str):
        strings_with_hash: tp.Optional[tp.Deque[str]] = self.direct_adress_table[self.hash(key_str)]
        if strings_with_hash:
            try:
                strings_with_hash.remove(key_str)
            except ValueError:
                pass

    def check(self, idx: int):
        if self.direct_adress_table[idx]:
             print(" ".join(self.direct_adress_table[idx]))
        else:
            print()

    def __str__(self):
        result_str = ""
        for i, value in enumerate(self.direct_adress_table):
            if value:
                result_str += f"idx={i} {value} "
        return result_str