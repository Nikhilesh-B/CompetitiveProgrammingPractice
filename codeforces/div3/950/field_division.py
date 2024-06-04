def binary_search(lst, target):
    lo = 0
    hi = len(lst) - 1
    while lo <= hi:
        mid = (lo+hi)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
    
def remove_pos(pos, horizontal_pos):
    idx = binary_search(horizontal_pos, pos)
    assert idx != -1
    horizontal_pos.pop(idx)
    return

def compute_initial(n, m, k, statues):
    horizontal_pos = [s[1] for s in statues]
    horizontal_pos.sort()

    statues_pos = [(i,s[1],s[0]) for i, s in enumerate(statues)]
    min_positions = {} 
    for idx, x, y in statues_pos:
        if y not in min_positions:
            min_positions[y] = [x]
        else:
            min_positions[y].append(x)

    max_x_pos_per_row = [0 for _ in range(n)]

    for i in range(n):
        if horizontal_pos:
            max_x_pos_per_row[i] = horizontal_pos[0]-1 
        else:
            max_x_pos_per_row[i] = m
        if i+1 in min_positions:
            delete_vals = min_positions[i+1]
            for val in delete_vals:
                remove_pos(val, horizontal_pos)

    total = 0
    for i in range(n):
        total += max_x_pos_per_row[i]
    print(total)
    return max_x_pos_per_row, total, min_positions

def compute_delta(max_pos_per_row, statue_pos, total, min_positions):
    copy_max_pos_per_row = max_pos_per_row.copy()
    x = statue_pos[1]
    y = statue_pos[2]
    for i in range(len(copy_max_pos_per_row)-1,-1,-1):
        if i == y-1:
            if len(min_positions[i+1])>2:
                sorted_min_positions = sorted(min_positions[i+1])
                copy_max_pos_per_row[i] += (sorted_min_positions[1]-sorted_min_positions[0])
            else:
                if i ==len(copy_max_pos_per_row)-1:
                    copy_max_pos_per_row[i] = m
                else:
                    copy_max_pos_per_row[i] = copy_max_pos_per_row[i+1]
        elif copy_max_pos_per_row[i] == x-1:
            if i+1 in min_positions:
                sorted_min_positions = sorted(min_positions[i+1])
                copy_max_pos_per_row[i] = min(copy_max_pos_per_row[i+1], sorted_min_positions[0]-1)
            else:
                copy_max_pos_per_row[i] = copy_max_pos_per_row[i+1] 

    return sum(copy_max_pos_per_row)-total


def compute_increase(n, m, k, statues, max_pos_per_row, total, min_positions):
    increase_decrease = [0 for _ in range(k)]
    magnitude_of_increase_decrease = [0 for _ in range(k)]

    horizontal_pos = [s[1] for s in statues]
    horizontal_pos.sort()
    
    statues_pos = [(i,s[1],s[0]) for i, s in enumerate(statues)]
    sorted_pos = sorted(statues_pos,key=lambda x: (x[2],-x[1]))
    
    for idx, x, y in sorted_pos:
        if x==m and y==1:
            remove_pos(x, horizontal_pos)
            continue 
        if len(horizontal_pos) > 1: 
            min_pos = horizontal_pos[0]
            second_min_pos = horizontal_pos[1]
            if x == min_pos and x < second_min_pos:
                increase_decrease[idx] = 1
        else:
            increase_decrease[idx] = 1
        remove_pos(x, horizontal_pos)


    for idx, val in enumerate(increase_decrease):
        if val == 1:
            magnitude_of_increase_decrease[idx] = compute_delta(max_pos_per_row, statues_pos[idx], total, min_positions)
        else:
            magnitude_of_increase_decrease[idx] = 0
    for i in magnitude_of_increase_decrease:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    t = int(input())
    n_s = {}
    m_s = {}
    k_s = {}
    statues_pos = {}

    for i in range(t):
        n, m, k = map(int, input().split())
        n_s[i] = n
        m_s[i] = m
        k_s[i] = k
        for j in range(k):
            if j == 0:
                statues_pos[i] = [list(map(int, input().split()))]
            else:
                statues_pos[i].append(list(map(int, input().split())))
    
    for i in range(t):
        n, m, k = n_s[i], m_s[i], k_s[i]
        statues = statues_pos[i]
        max_pos_per_row, total, min_positions = compute_initial(n, m, k, statues)
        compute_increase(n, m, k, statues, max_pos_per_row, total, min_positions)