from collections import deque


def main():

    buffer_size, n = map(int, input().strip().split(" "))
    deq = deque([-1 for _ in range(buffer_size)], buffer_size)

    for _ in range(n):
        arrival_time, duration_time = map(int, input().strip().split(" "))
        if arrival_time < deq[0]:
            print(-1)
        else:
            last_element_end_time = deq[-1] if deq[-1] != -1 else 0
            print(max(last_element_end_time, arrival_time))
            current_element_end_time = max(last_element_end_time, arrival_time) + duration_time
            deq.popleft()
            deq.append(current_element_end_time)
            # print(deq)

if __name__ == "__main__":
    main()