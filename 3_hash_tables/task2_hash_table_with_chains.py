
from custom_data_structures.hash_table import HashTable

def main():
    m = int(input().strip())
    n = int(input().strip())
    table = HashTable(m)
    for _ in range(n):
        cmd = input().strip()
        if cmd.startswith("add"):
            string = cmd.split(" ")[1]
            table.add(string)
        elif cmd.startswith("find"):
            string = cmd.split(" ")[1]
            table.find(string)
        elif cmd.startswith("del"):
            string = cmd.split(" ")[1]
            table.delete(string)
        elif cmd.startswith("check"):
            i: int = int(cmd.split(" ")[1])
            table.check(i)

if __name__ == "__main__":
    main()