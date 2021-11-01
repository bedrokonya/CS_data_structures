import math
import typing as tp


def sift_down(A: tp.List[int], idx: int, result: tp.List[str]) -> int:
    current_idx: int = idx
    heap_size: int = len(A)
    while get_left_child_idx(current_idx) < heap_size:
        l_idx = get_left_child_idx(current_idx)
        r_idx = get_right_child_idx(current_idx)
        min_idx = l_idx
        if r_idx < heap_size and A[r_idx] < A[l_idx]:
            min_idx = r_idx
        if A[min_idx] < A[current_idx]:
            A[min_idx], A[current_idx] = A[current_idx], A[min_idx]
            result.append(f"{min_idx} {current_idx}")
            current_idx = min_idx
        else:
            break


def get_parent_idx(i: int) -> int:
    return math.floor(i - 1 / 2)


def get_left_child_idx(i: int) -> int:
    return 2 * i + 1


def get_right_child_idx(i: int) -> int:
    return 2 * i + 2


def build_heap(A: tp.List[int]) -> None:
    heap_size: int = len(A)
    result = []
    for i in range(heap_size // 2, -1, -1):
        sift_down(A, i, result)
    return result



def is_min_heap(A: tp.List[int]) -> bool:
    heap_size: int = len(A)
    for i in range(heap_size):
        l: int = get_left_child_idx(i)
        r: int = get_left_child_idx(i)
        if l < heap_size and A[i] > A[l]:
            return False
        if r < heap_size and A[i] > A[r]:
            return False
    return True


def main():
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    result = build_heap(A)
    print(len(result))
    for string in result:
        print(string)

if __name__ == "__main__":
    main()