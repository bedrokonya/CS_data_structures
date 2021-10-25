from heapq import heappop, heappush


def main():
    n, m = map(int, input().strip().split(" "))
    if n == 0 or m == 0:
        return
    tasks_duration = list(map(int, input().strip().split(" ")))
    assert len(tasks_duration) == m

    priority_queue = [(0, j) for j in range(n)]
    for duration in tasks_duration:
        release_time, n_processor = heappop(priority_queue)
        print(f"{n_processor} {release_time}")
        heappush(priority_queue, (release_time + duration, n_processor))

if __name__ == "__main__":
    main()