# from stack import Stack

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

    # def _get_copied_value(self, value: T) -> T:
    #     copy_op = getattr(value, "copy", None)
    #     return copy_op(value) if callable(copy_op) else value





OPEN_BRACKETS = ["(", "{", "["]
CLOSE_BRACKETS = [")", "}", "]"]
BRACKETS_DICT = {")": "(",
                 "}": "{",
                 "]": "["}


def main():

    stack_char: Stack = Stack()
    stack_index: Stack = Stack()
    code_string: str = input().strip()

    for i, char in enumerate(code_string):
        if char in OPEN_BRACKETS:
            stack_char.push(char)
            stack_index.push(i)
        elif char in CLOSE_BRACKETS:
            if BRACKETS_DICT[char] == stack_char.top():
                stack_char.pop()
                stack_index.pop()
            else:
                print(i + 1)
                return
        else:
            continue

    if not stack_char.is_empty():
        assert not stack_index.is_empty()
        print(stack_index.bottom() + 1)
        return

    print("Success")


if __name__ == "__main__":
    main()
