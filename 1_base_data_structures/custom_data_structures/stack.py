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



