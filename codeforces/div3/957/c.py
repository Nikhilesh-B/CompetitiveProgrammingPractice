t = int(input())
answers = []

for _ in range(t):
    n_m_k = list(map(int, input().split()))
    n = n_m_k[0]
    m = n_m_k[1]
    k = n_m_k[2]

    top_half = [x for x in range(n, m, -1)]
    bottom_half = [y for y in range(1, m+1)]

    answers.append(top_half + bottom_half)


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


for answer in answers:
    print_array(answer)
