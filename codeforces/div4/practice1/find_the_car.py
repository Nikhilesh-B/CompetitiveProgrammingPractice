import bisect

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n_k_q = input()
        n, k, q = list(map(int, n_k_q.split()))
        distances = list(map(int, input().split()))
        times = list(map(int, input().split()))
        distances.insert(0, 0)
        times.insert(0, 0)
        for i in range(q):
            if i == q-1:
                end_str = "\n"
            else:
                end_str = ""

            query_distance = int(input())
            right_idx = bisect.bisect_left(distances, query_distance)
            left_idx = right_idx - 1
            if distances[right_idx] == query_distance:
                print(times[right_idx], end=end_str)
            elif distances[left_idx] == query_distance:
                print(times[left_idx], end=end_str)
            else:
                speed_between_points = (
                    distances[left_idx] - distances[right_idx]) / (times[left_idx] - times[right_idx])
                time_to_reach_from_left_idx = (
                    query_distance - distances[left_idx]) / speed_between_points
                print(int(times[left_idx] + time_to_reach_from_left_idx))
