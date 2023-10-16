
def process_nums(nums):
    ones = dict()  # keyed on each individual index
    zeroes = dict()  # keyed on each individual index
    for i, num_string in enumerate(nums):
        for j, char in enumerate(num_string):
            if char == "1":
                if j not in ones:
                    ones[j] = [i]
                else:
                    ones[j].append(i)
            else:
                if j not in zeroes:
                    zeroes[j] = [i]
                else:
                    zeroes[j].append(i)

    for j in range(29):
        if j not in ones:
            ones[j] = []
        if j not in zeroes:
            zeroes[j] = []

    return ones, zeroes


def isPossible(l, r, ones, zeroes, k):
    current_subset = None
    for i, char in enumerate(k):
        if char == "1":
            if current_subset is None:
                current_subset = set()
                print(ones)
                for idx in ones[i]:
                    if idx >= l and idx <= r:
                        current_subset.add(idx)
            else:
                current_subset = current_subset.intersection(set(ones[i]))
                if not current_subset.intersection(set(zeroes[i])):
                    return False

    # this logic is wrong
    for i, char in enumerate(k):
        if char == "0":
            if current_subset is None:
                current_subset = set()
                for idx in zeroes[i]:
                    if idx >= l and idx <= r:
                        current_subset.add(idx)
            else:
                if not current_subset.intersection(set(zeroes[i])):
                    return False

    return bool(current_subset)


def run_queries(queries, ones, zeroes, k):
    for q in queries:
        l, r = q[0], q[1]
        if isPossible(l, r, ones, zeroes, k):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    n_k_q = input().split(" ")
    n, k, q = n_k_q[0], n_k_q[1], n_k_q[2]
    n, k, q = int(n), int(k), int(q)

    k = "0"*(29-len(str(bin(int(k))[2:])))+str(bin(int(k))[2:])
    nums = input().split(" ")
    nums = ["0"*(29-len(str(bin(int(num))[2:]))) +
            str(bin(int(num))[2:]) for num in nums]
    queries = []

    for _ in range(q):
        l_r = input().split(" ")
        l, r = int(l_r[0])-1, int(l_r[1])-1
        queries.append((l, r))

    ones, zeroes = process_nums(nums=nums)
    run_queries(queries=queries, ones=ones, zeroes=zeroes, k=k)
