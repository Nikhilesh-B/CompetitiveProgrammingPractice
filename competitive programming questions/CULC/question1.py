def calculate_val(n, k, qualities):
    qualities.sort(reverse=True)
    answer = sum(qualities)+sum(qualities[:k])
    return answer


if __name__ == "__main__":
    n_k_str = input()
    qualities = input().split(" ")
    n, k = n_k_str.split(" ")[0], n_k_str.split(" ")[1]
    n, k = int(n), int(k)
    qualities = [int(q) for q in qualities]
    print(calculate_val(n, k, qualities))
