if __name__ == "__main__":
    t = int(input())
    cases = {}
    for i in range(t):
        n = int(input())
        lst_a = tuple(list(map(int, input().split())))
        lst_b = tuple(list(map(int, input().split())))
        cases[i] = (n, lst_a, lst_b)

    for i in range(t):
        n = cases[i][0]
        lst_a = list(cases[i][1])
        lst_b = list(cases[i][2])

        total_moves = 0

        for j in range(n):
            total_moves += abs(lst_a[j]-lst_b[j])

        last_val_in_b = lst_b[-1]

        closest_val = 10**10
        for j in range(n):
            if closest_val > abs(lst_a[j]-last_val_in_b):
                closest_val = abs(lst_a[j]-last_val_in_b)
            if closest_val > abs(lst_b[j]-last_val_in_b):
                closest_val = abs(lst_b[j]-last_val_in_b)

        total_moves += (closest_val+1)
        print(total_moves)
