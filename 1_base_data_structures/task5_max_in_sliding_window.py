from collections import deque


class Stack(deque):
    def __init__(self, maxlen=None):
        super(Stack, self).__init__(maxlen=maxlen)

    def top(self):
        return self.__getitem__(self.__len__() - 1)[0] if self.__len__() > 0 else None

    def push(self, element):
        current_max = max(element, self.max()) if self.__len__() > 0 else element
        self.append((element, current_max))

    def pop(self):
        return super().pop()[0]

    def max(self):
        return self.__getitem__(self.__len__() - 1)[1] if self.__len__() > 0 else None

    def is_empty(self):
        return self.__len__() == 0


class QueueOnStacks:
    def __init__(self, max_stack_size=None):
        self.stack_in = Stack(max_stack_size)
        self.stack_out = Stack(max_stack_size)

    def put(self, elem):
        self.stack_in.push(elem)

    def get(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def max(self):
        stack_in_max = self.stack_in.max()
        stack_out_max = self.stack_out.max()
        if stack_in_max is None:
            return stack_out_max
        if stack_out_max is None:
            return stack_in_max
        return max(stack_in_max, stack_out_max)

def main():
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    m = int(input())
    q = QueueOnStacks(m)

    for i in range(m):
        q.put(A[i])

    print(q.max())

    for i in range(m, n):
        q.get()
        q.put(A[i])
        print(q.max())





if __name__ == "__main__":
    main()