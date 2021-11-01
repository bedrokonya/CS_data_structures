from custom_data_structures.hash_table import HashTable


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


if __name__ == "__main__":
    main()