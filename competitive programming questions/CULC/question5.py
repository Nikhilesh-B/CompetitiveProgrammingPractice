# we need to run some faster operations here

def memoized_exponentation_calc(exponentations, n):
    if n in exponentations:
        val = exponentations[n]
        return val
    else:
        val = memoized_exponentation_calc(exponentations=exponentations, n=n-1)
        exponentations[n] = 2*val
        return 2*val


def calculate_val(input_string):
    n = len(input_string)
    input_string = input_string[::-1]
    running_sum = 0
    exponentations = {0: 1}
    for i, char in enumerate(input_string):
        if char == "O":
            if i not in exponentations:
                val = memoized_exponentation_calc(exponentations, i)
                exponentations[i] = val
            else:
                val = exponentations[i]
            running_sum += (val)
    return running_sum % (10**9+7)


if __name__ == "__main__":
    input_str = input()
    print(calculate_val(input_str))
