import typing as tp

T = tp.TypeVar('T')


class QueueSizeFixed(tp.Generic[T]):
    def __init__(self, size: int):
        self.capacity = size
        self.current_size = 0
        self.begin_index = 0
        self.end_index = 0
        self.values = [None for _ in range(self.capacity)]

    def enqueue(self, value: T) -> bool:
        if self.current_size >= self.capacity:
            return False
        self.values[self.end_index] = value
        self.current_size += 1
        self.end_index = (self.end_index + 1) % self.capacity
        return True

    def dequeue(self) -> T:
        if self.current_size == 0:
            return None
        result = self.values[self.begin_index]
        self.begin_index = (self.begin_index + 1) % self.capacity
        self.current_size -= 1
        return result

    def is_empty(self) -> bool:
        return self.current_size == 0

    def __str__(self):
        string = f"begin_index={self.begin_index}, end_index={self.end_index} capacity={self.capacity} current_size={self.current_size}\n"
        for i in range(self.begin_index, self.end_index):
            if self.values[i]:
                string += f" | value {self.values[i]}, index={i} | "
        return string


def main():
    q = QueueSizeFixed(10)
    q.enqueue(10)
    print(q)
    q.enqueue(20)
    print(q)
    q.enqueue(30)
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()

if __name__ == "__main__":
    main()
