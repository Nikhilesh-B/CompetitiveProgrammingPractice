t = int(input())

answers = []

for _ in range(t):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]
    reference = []
    for _ in range(n):
        num_str = input()
        nums = [int(num) for num in num_str]
        reference.append(nums)

    matrix = [[0 for _ in range(n//k)] for _ in range(n//k)]

    for i, r in enumerate(range(0, n, k)):
        for j, c in enumerate(range(0, n, k)):
            matrix[i][j] = reference[r][c]
    answers.append(matrix)


def print_matrix(mat):
    for row in mat:
        print("".join(map(str, row)))


for ans in answers:
    print_matrix(ans)
