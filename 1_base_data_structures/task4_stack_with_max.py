import typing as tp

T = tp.TypeVar('T')


class Stack(tp.Generic[T]):
    def __init__(self):
        self.values = []
        self.length = 0

    def top(self) -> T:
        return self.values[self.length - 1] if self.length > 0 else None

    def bottom(self) -> T:
        return self.values[0] if self.length > 0 else None

    def is_empty(self) -> bool:
        return self.length == 0

    def pop(self) -> T:
        value = self.values.pop(self.length - 1) if self.length > 0 else None
        self.length -= 1
        return value

    def push(self, value: T):
        self.values.append(value)
        self.length += 1

    def __str__(self):
        return f"length={self.length}\nvalues: {[self.values[i] for i in range(len(self.values))]}"

class StackWithMax(Stack):
    def __init__(self):
        super(StackWithMax, self).__init__()
        self.local_max = []

    def max(self) -> T:
        return self.local_max[self.length - 1] if self.length > 0 else None

    def pop(self) -> T:
        if self.length > 0:
            self.local_max.pop(self.length - 1)
        return super(StackWithMax, self).pop()

    def push(self, value: T):
        current_top_max = self.local_max[self.length - 1] if self.length > 0 else None
        current_max = max(value, current_top_max) if current_top_max else value
        self.local_max.append(current_max)
        super(StackWithMax, self).push(value)

    def __str__(self):
        result = super(StackWithMax, self).__str__()
        result += f"\nmax_values: {[self.local_max[i] for i in range(len(self.local_max))]}"
        return result


def main():

    q = int(input())
    s = StackWithMax()
    for _ in range(q):
        tokens = input().strip().split(" ")
        cmd = tokens[0]
        try:
            value = int(tokens[1])
        except IndexError:
            value = None

        if cmd == "pop":
            s.pop()
        if cmd == "push":
            s.push(value)
        if cmd == "max":
            print(s.max())


if __name__ == "__main__":
    main()


