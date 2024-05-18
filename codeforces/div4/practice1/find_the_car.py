import bisect

if __name__ == "__main__":
    n_k_qs = []
    arr_distances = []
    arr_times = []
    t = int(input())
    for _ in range(t):
        n_k_q = input()
        n_k_qs.append(n_k_q)
        distances = list(map(int, input().split()))
        times = list(map(int, input().split()))
        distances.insert(0, 0)
        times.insert(0, 0)
        arr_distances.append(distances)
        arr_times.append(times)


    for i in range(t):
        n_k_q = n_k_qs[i]
        distances = arr_distances[i]
        times = arr_times[i]
        n, k, q = map(int, n_k_q.split())
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
