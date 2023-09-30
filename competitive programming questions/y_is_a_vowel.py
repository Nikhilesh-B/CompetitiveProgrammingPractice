def compute_results():
    string = input()
    t1, t2 = 0, 0

    for char in string:
        if char in ['a','e','i','o','u']:
            t1 +=1
        if char in ['a','e','i','o','u','y']:
            t2 +=1

    return t1, t2


if __name__ == "__main__":
    t1, t2 = compute_results()
    print(t1, t2)
