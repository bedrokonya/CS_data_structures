from custom_data_structures.stack import Stack

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
