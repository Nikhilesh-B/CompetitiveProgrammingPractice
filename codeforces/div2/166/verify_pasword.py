def no_digit_after_letter(case: str):
    for i in range(len(case) - 1):
        if case[i].isalpha() and case[i+1].isdigit():
            return False
    return True


def all_digits_non_decreasing(case: str):
    chars = []
    for char in case:
        if char.isdigit():
            chars.append(int(char))

    return chars == sorted(chars)


def all_letters_non_decreasing(case: str):
    chars = []
    for char in case:
        if char.isalpha():
            chars.append(char)

    return chars == sorted(chars)


def is_valid(case):
    first_condition = no_digit_after_letter(case)
    second_condition = all_digits_non_decreasing(case)
    third_condition = all_letters_non_decreasing(case)
    if first_condition and second_condition and third_condition:
        return True
    return False


if __name__ == '__main__':
    t = int(input())
    cases = []
    for _ in range(t):
        n = int(input())
        p = input()
        cases.append(p)

    for case in cases:
        if is_valid(case):
            print("YES")
        else:
            print("NO")
