import typing as tp


class Node:
    def __init__(self,
                 value: tp.Any,
                 parent: tp.Optional["Node"] = None,
                 is_left: tp.Optional[bool] = None,
                 left_child: tp.Optional["Node"] = None,
                 right_child: tp.Optional["Node"] = None):

        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
        self.is_left = is_left

        self.sum = self.value
        self.size = None
        self.update_metrics()

    def update_metrics(self):
        self.count_size()
        self.count_sum()

    def count_size(self):
        self.size = 1
        if self.left_child:
            self.size += self.left_child.size
        if self.right_child:
            self.size += self.right_child.size

    def count_sum(self):
        self.sum = self.value
        if self.left_child:
            self.sum += self.left_child.sum
        if self.right_child:
            self.sum += self.right_child.sum

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        str_to_display: str = f'({self.value})' if self.size is None else f'({self.value} {self.size})'
        # No child.
        if self.right_child is None and self.left_child is None:
            line = str_to_display
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right_child is None:
            lines, n, p, x = self.left_child._display_aux()
            s = str_to_display
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left_child is None:
            lines, n, p, x = self.right_child._display_aux()
            s = str_to_display
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left_child._display_aux()
        right, m, q, y = self.right_child._display_aux()
        s = str_to_display
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
