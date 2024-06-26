import heapq


def process_case(n, arr):
    ans = [0 for _ in range(n)]
    pq = []
    curr_sum = 0
    for idx, num in enumerate(arr):
        heapq.heappush(pq, -num)
        curr_sum += num
        if curr_sum + pq[0] == -pq[0]:
            ans[idx] = 1
    print(sum(ans))


if __name__ == "__main__":
    t = int(input())
    n_s = []
    arrs = []

    for _ in range(t):
        n = int(input())
        n_s.append(n)
        arr = list(map(int, input().split()))
        arrs.append(arr)

    for i in range(t):
        n = n_s[i]
        arr = arrs[i]
        process_case(n, arr)
