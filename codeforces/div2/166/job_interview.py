
def base_case_answer(n, m, a_list, b_list):
    n_count = 0
    m_count = 0
    total_n = 0
    total_m = 0

    pivot_idx = None
    saturated = None
    for i in range(n+m):
        if n_count == n:
            pivot_idx = i
            saturated = 'n'
            total_m += b_list[i]
            m_count += 1
            continue
        if m_count == m:
            pivot_idx = i
            saturated = 'm'
            total_n += a_list[i]
            n_count += 1
            continue

        if a_list[i] > b_list[i]:
            total_n += a_list[i]
            n_count += 1

        if a_list[i] < b_list[i]:
            total_m += b_list[i]
            m_count += 1

    return total_n+total_m, pivot_idx, saturated


def left_hand_side_process(n, m, a_list, b_list, left_idx, pivot_idx, base_case, saturated, left_critical_value, left_base_case):
    if saturated == 'n':
        if b_list[left_idx] > b_list[left_idx]:
            return base_case-b_list[left_idx]+b_list[n+m]
        else:
            return left_base_case-b_list[left_idx]+left_critical_value
    else:
        if a_list[left_idx] > a_list[pivot_idx]:
            return base_case-a_list[left_idx]+a_list[n+m]
        else:
            return left_base_case-b_list[left_idx]+left_critical_value


def right_hand_side_process(n, m, a_list, b_list, right_idx, base_case, saturated):
    if saturated == 'n':
        return base_case-b_list[right_idx]+b_list[n+m]

    else:
        return base_case-a_list[right_idx]+a_list[n+m]


def left_critical_value(n, m, a_list, b_list, pivot_idx, saturated):
    total = 0
    if saturated == 'n':
        for i in range(pivot_idx, n+m+1):
            if a_list[i] > b_list[i]:
                total += a_list[i]
                for j in range(i, n+m):
                    total += b_list[j]
                break
            else:
                total += b_list[i]

    else:
        for i in range(pivot_idx, n+m+1):
            if a_list[i] < b_list[i]:
                total += b_list[i]
                for j in range(i, n+m):
                    total += a_list[j]
                break
            else:
                total += a_list[i]
    return total


def left_base_value(n, m, a_list, b_list, pivot_idx, saturated):
    total = 0
    for i in range(0, pivot_idx):
        if a_list[i] > b_list[i]:
            total += a_list[i]
        else:
            total += b_list[i]

    return total


def process_case(n, m, a_list, b_list):
    answers = [0 for _ in range(n+m+1)]
    base_case, pivot_idx, saturated = base_case_answer(n, m, a_list, b_list)
    lbv = left_base_value(n, m, a_list, b_list, pivot_idx, saturated)
    lcv = left_critical_value(n, m, a_list, b_list, pivot_idx, saturated)
    answers[-1] = base_case

    print("BASE CASE: ", base_case)
    print("PIVOT IDX: ", pivot_idx)

    for i in range(n+m-1):
        if i < pivot_idx:
            answers[i] = left_hand_side_process(
                n, m, a_list, b_list, i, pivot_idx, base_case, saturated, lcv, lbv)
        else:
            answers[i] = right_hand_side_process(
                n, m, a_list, b_list, i, base_case, saturated)

    # print answers
    for i, answer in enumerate(answers):
        if i != len(answers)-1:
            print(answer, end=" ")
        else:
            print(answer)


if __name__ == "__main__":
    t = int(input())
    cases = {}

    for i in range(t):
        n_m_list = list(map(int, input().split()))
        n = n_m_list[0]
        m = n_m_list[1]
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))
        cases[i] = (n, m, a_list, b_list)

    for i in range(t):
        n = cases[i][0]
        m = cases[i][1]
        a_list = list(cases[i][2])
        b_list = list(cases[i][3])
        process_case(n, m, a_list, b_list)
