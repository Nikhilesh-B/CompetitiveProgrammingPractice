
def compute():
    n_lph_list = input().split(" ")
    n, lph = int(n_lph_list[0]),int(n_lph_list[1])
    tl = lph*5
    list_of_problems = []

    for _ in range(n):
        len_problem = int(input())
        list_of_problems.append(len_problem)

    list_of_problems.sort()
    count = 0
    for problem_len in list_of_problems:
        if tl - problem_len < 0:
            break
        else:
            tl -= problem_len
            count += 1
    print(count)


if __name__ == "__main__":
    compute()
