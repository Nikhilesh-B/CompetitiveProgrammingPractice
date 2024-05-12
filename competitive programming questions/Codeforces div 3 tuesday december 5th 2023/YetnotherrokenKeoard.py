def process_presses(key_press):
    r_str = ""
    UC_stack = []
    LC_stack = []
    for i, char in enumerate(key_press):
        if char == "B" and UC_stack:
                UC_stack.pop(-1)
        elif char == 'b' and LC_stack:
                LC_stack.pop(-1)
        else:
            if char.isupper():
                UC_stack.append((char, i))
            else:
                LC_stack.append((char, i))

    while UC_stack or LC_stack:
        if UC_stack and LC_stack:
            if UC_stack[-1][1] > LC_stack[-1][1]:
                r_str = UC_stack.pop(-1)[0]+r_str
            else:
                r_str = LC_stack.pop(-1)[0]+r_str
        elif UC_stack:
            r_str = UC_stack.pop(-1)[0]+r_str
        elif LC_stack:
            r_str = LC_stack.pop(-1)[0]+r_str

    print(r_str)


if __name__ == "__main__":
    n_test_cases = int(input())
    kps = []
    while n_test_cases > 0:
        key_press = input()
        kps.append(key_press)
        n_test_cases -= 1

    for kp in kps:
        process_presses(kp)
