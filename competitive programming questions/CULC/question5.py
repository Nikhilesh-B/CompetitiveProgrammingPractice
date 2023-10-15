# we need to run some faster operations here

def calculate_val(input_string):
    n = len(input_string)
    input_string = input_string[::-1]
    running_sum = 0
    prev_exponentation = 1
    prev_expon_idx = 0
    for i, char in enumerate(input_string):
        if char == "O":
            prev_exponentation = 2**(i-prev_expon_idx) * \
                prev_exponentation % (10**9+7)
            prev_expon_idx = i
            running_sum += prev_exponentation
    return running_sum


if __name__ == "__main__":
    input_str = input()
    print(calculate_val(input_str))
